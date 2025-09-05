from typing import List
from app.extensions import db, login_manager
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import mapped_column, relationship, Mapped
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin

class User(db.Model, UserMixin):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(30), nullable=False, unique=True)
    password_hash: Mapped[str] = mapped_column(String(256))
    email: Mapped[str] = mapped_column(String(120), index=True, unique=True, nullable=False)
    isBanned: Mapped[bool] = mapped_column(nullable=False, default=False)
    questions: Mapped["Question"] = relationship(back_populates="author")

    def set_password(self, password: str) -> None:
        self.password_hash = generate_password_hash(password=password)

    def check_password(self, password: str) -> None:
        return check_password_hash(self.password_hash, password=password)

    def __repr__(self) -> str:
        return f"<User id={self.id} username={self.username} email={self.email}>"

@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))

class Course(db.Model):
    __tablename__ = "course"

    id: Mapped[int] = mapped_column(primary_key=True)
    questions: Mapped[List["Question"]] = relationship(back_populates="course")
    name: Mapped[str] = mapped_column(nullable=False)

class Question(db.Model):
    __tablename__ = "question"

    id: Mapped[int] = mapped_column(primary_key=True)

    course_id: Mapped[int] = mapped_column(ForeignKey("course.id"))
    course: Mapped[Course] = relationship(back_populates="questions")

    author_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    author: Mapped[User] = relationship(back_populates="questions")

    grade_level: Mapped[int] = mapped_column(nullable=False)
