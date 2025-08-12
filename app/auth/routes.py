from urllib.parse import urlsplit
from flask_login import current_user, login_required, login_user, logout_user
from app.models import User
import sqlalchemy as sa
from app.extensions import db
from flask import flash, redirect, render_template, url_for, request
from . import auth_bp
from .form import LoginForm, RegisterForm

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        select_stmt = sa.select(User).where(User.username == form.username.data)
        user = db.session.scalar(select_stmt)
        if not user or user.check_password(user.password_hash):
            flash("Invalid Username or Password")
            return redirect(url_for("auth.login"))
        login_user(user)
        next = request.args.get("next")
        if not next or urlsplit(next).netloc != "" or next == "/":
            return redirect(url_for("web.index"))
        return redirect(next)
    return render_template("login.html", form=form)

@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    return render_template("register.html", form=form)
