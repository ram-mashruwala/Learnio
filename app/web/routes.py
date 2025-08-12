from flask import render_template, url_for
from flask_login import login_required
from . import web_bp

@web_bp.route('/index')
@web_bp.route('/')
@login_required
def index():
    return render_template("index.html")
