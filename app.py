from flask import Flask
from flask import Flask, redirect, render_template, request, url_for, send_from_directory, send_file
import os
import sys
from FeaturedImageCreatorService.FeaturedImageCreatorService import FeaturedImageCreatorService
from werkzeug.exceptions import HTTPException, Forbidden, NotFound, RequestTimeout, Unauthorized


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():

    title = ""
    subtitle = ""
    imageurl = "https://pixabay.com/photos/the-alps-switzerland-mountains-4817766/"
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


@app.errorhandler(NotFound)
def page_not_found_handler(e: HTTPException):
    return render_template('404.html'), 404


@app.errorhandler(Unauthorized)
def unauthorized_handler(e: HTTPException):
    return render_template('401.html'), 401


@app.errorhandler(Forbidden)
def forbidden_handler(e: HTTPException):
    return render_template('403.html'), 403


@app.errorhandler(RequestTimeout)
def request_timeout_handler(e: HTTPException):
    return render_template('408.html'), 408


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')