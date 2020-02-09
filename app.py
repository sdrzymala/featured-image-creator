from flask import Flask
from flask import Flask, redirect, render_template, request, url_for, send_from_directory, send_file
import os
import sys
from FeaturedImageCreatorService.FeaturedImageCreatorService import FeaturedImageCreatorService
import git




app = Flask(__name__)




if __name__ == "__main__":
    app.run()


@app.route('/update_project', methods=['POST'])
def webhook():
    if request.method == 'POST':
        repo = git.Repo('/home/sdrzymala/featured-image-creator/')
        origin = repo.remotes.origin


@app.route("/", methods=["GET", "POST"])
def index():

    title = ""
    subtitle = ""
    imageurl = ""
    generate_image_path = ""
    show_featured_image = False

    if request.method == "GET":
        response_msg = ""
        completed_succesfully = None
        generate_image_path = ""
        show_featured_image = False
        
    elif request.method == "POST":
        title = request.form["title"]
        subtitle = request.form["subtitle"]
        imageurl = request.form["imageurl"]
    
        s = FeaturedImageCreatorService()
        generate_image_path, completed_succesfully, response_msg = s.generate_featured_image(title, subtitle, imageurl)
        
        if completed_succesfully:
            show_featured_image = True
    
    return render_template("main_page.html", completed_succesfully=completed_succesfully, generate_image_path = generate_image_path, show_featured_image=show_featured_image, title = title, subtitle = subtitle, imageurl = imageurl,response_msg = response_msg)




@app.route("/download", methods=["GET", "POST"])
def download():
    
    image_to_download_path = request.form["output_image_path"]
    return send_file(image_to_download_path, as_attachment=True)