from typing import Any
from database import db
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.sql import func


class Base(DeclarativeBase):
    pass


class Meal(db.Model):

    __tablename__ = 'Meal'
    id: Mapped[int] = db.Column(db.Integer, primary_key=True)
    title: Mapped[str] = db.Column(
        db.String(120), unique=False, nullable=False)
    description: Mapped[str] = db.Column(db.Text, unique=False)
    created_at: Mapped[str] = db.Column(db.DateTime(timezone=True),
                                        server_default=func.now())
    last_updated: Mapped[str] = db.Column(
        db.DateTime(timezone=True), unique=False,
        server_default=func.now())
    in_diet: Mapped[bool] = db.Column(db.Boolean, unique=False, nullable=False)
    owner_id: Mapped[int] = db.Column(db.Integer, db.ForeignKey('user.id'))
