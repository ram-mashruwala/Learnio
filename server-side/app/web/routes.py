from flask import render_template, url_for
from flask_login import login_required
from . import web_bp

@web_bp.route('/index')
@web_bp.route('/')
# @login_required
def index():
    return     "<form action='/upload' method='post' enctype='multipart/form-data'> <label for='file-upload'>Choose a file:</label> <input type='file' id='file-upload' name='uploaded_file'> <button type='submit'>Upload</button> </form>"
