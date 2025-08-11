from flask import Flask
from config import Config

# Initializing flask app object
app = Flask(__name__)
app.config.from_object(Config)

# Initializing additional flask objects
from app.extensions import db, login_manager, migrate
db.init_app(app=app)
migrate.init_app(app=app, db=db)
login_manager.init_app(app=app)
login_manager.login_view = "auth.login"

# Registering Blueprints
from app.api import api_bp
from app.web import web_bp
from app.auth import auth_bp
app.register_blueprint(web_bp)
app.register_blueprint(api_bp)
app.register_blueprint(auth_bp)
