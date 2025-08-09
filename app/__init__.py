from flask import Flask

from app.api import api_bp
from app.web import web_bp

app = Flask(__name__)

app.register_blueprint(web_bp)
app.register_blueprint(api_bp)
