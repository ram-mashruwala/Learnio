from flask import Flask
from app.extensions import db, migrate
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app=app)
migrate.init_app(app=app, db=db)

from app.api import api_bp
from app.web import web_bp
app.register_blueprint(web_bp)
app.register_blueprint(api_bp)
