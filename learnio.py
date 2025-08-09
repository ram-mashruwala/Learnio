from app import app
import sqlalchemy as sa
import sqlalchemy.orm as orm
from app.models import User
from app.extensions import db

@app.shell_context_processor
def make_shell_context():
    return {"sa": sa, "orm": orm, "db": db, "User": User}
