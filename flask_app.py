from flask import Flask
from flask import Flask, redirect, render_template, request, url_for, send_from_directory, send_file
from flask_autoindex import AutoIndex
import os
import sys
from FeaturedImageCreatorService.FeaturedImageCreatorService import FeaturedImageCreatorService

#vide: https://blog.pythonanywhere.com/121/

app = Flask(__name__)
app.config["DEBUG"] = True

return_code = ""
generate_image_path = ""
show_featured_image = False

@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == "GET":
        return_code = ""
        generate_image_path = ""
        show_featured_image = False
        
    elif request.method == "POST":
        title = request.form["title"]
        subtitle = request.form["subtitle"]
        s = FeaturedImageCreatorService()
        generate_image_path = s.generate_featured_image(title, subtitle)
        return_code = "Image generated succesfully"
        show_featured_image = True
    
    return render_template("main_page.html", return_status=return_code, generate_image_path = generate_image_path, show_featured_image=show_featured_image)

@app.route("/download", methods=["GET", "POST"])
def download():
    image_to_download_path = request.form["output_image_path"]
    return send_file(image_to_download_path, as_attachment=True)
    

if __name__ == "__main__":
    app.run()