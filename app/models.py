from app.extensions import db
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import mapped_column, relationship, Mapped
from werkzeug.security import check_password_hash, generate_password_hash

class User(db.Model):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(30), nullable=False, unique=True)
    password_hash: Mapped[str] = mapped_column(String(256))
    email: Mapped[str] = mapped_column(String(120), index=True, unique=True)

    def set_password(self, password: str) -> None:
        self.password_hash = generate_password_hash(password=password)

    def check_password(self, password: str) -> None:
        return check_password_hash(self.password_hash, password=password)

    def __repr__(self) -> str:
        return f"<User id={self.id} username={self.username} email={self.email}>"
