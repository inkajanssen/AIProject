from typing import List
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import relationship, Mapped, mapped_column

db = SQLAlchemy()


class User(db.Model):
    """
    Class for a user with:
        a unique identifier(user_id)
        a unique name(username)
        a list of created chars(max. 3)
    """
    __tablename__ = "users"

    user_id:Mapped[int] = mapped_column(primary_key = True)
    username:Mapped[str] = mapped_column(String(30), nullable = False, unique = True)

    created_chars:Mapped[List["Character"]] = relationship(back_populates="creator",
                                                           lazy= "dynamic", cascade= "all, delete-orphan")

    def __str__(self):
        return f"Username:{self.username} created following characters: {self.created_chars}"

    def __repr__(self):
        return f"ID: {self.user_id}, Name: {self.username}, Chars: {self.created_chars}"


class Character(db.Model):
    """
    Class for a user with:
        an unique identifier(char_id)
        a name (char_name)
        the user_id of the creator
        a relationship to the creator (creator)
        a picture TODO
        a skillset of:
            TODO
        possible items?TODO
        backstory TODO
    """
    __tablename__ = "characters"

    char_id:Mapped[int] = mapped_column(primary_key = True)
    char_name:Mapped[str] = mapped_column(String(100), nullable = False)
    user_id:Mapped[int] = mapped_column(ForeignKey("users.user_id"))
    creator:Mapped["User"] = relationship(back_populates="created_chars")

    def __str__(self):
        return f"Name: {self.name} has following skills:"

    def __repr__(self):
        return f"ID: {self.char_id}, Name: {self.char_name}"
