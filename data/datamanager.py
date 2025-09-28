from flask import session

from .models import db, User, Character

class DataManager:
    """
    TODO
    Class to interact with the SQLite database.
    """

    def create_user(self, username):
        """
        Add a new user to the database
        """
        user = User.query.filter_by(username=username).first()
        if user is None:
            new_user = User(username=username)
            db.session.add(new_user)
            db.session.commit()

            return "User successfully added to the database."
        return "User already in Database"


    def get_users(self):
        """
        Retrieve all Users to display them on homepage
        """
        users = User.query.order_by(User.username).all()
        if users:
            return users
        return []


    def delete_user(self, user_id):
        """
        Delete user from database
        """
        user = User.query.get(user_id)

        if not user:
            return "Error: User could not be found"

        db.session.delete(user)
        db.session.commit()
        return "User successfully deleted from database."


    def get_characters(self, user_id):
        """
        TODO
        Get all characters associated to user as a list
        """
        user = User.query.get(user_id)
        return user.created_chars.order_by(Character.char_name).all()


    def create_character(self, character, user_id):
        """
        Create a character and link it to user
        """
        user = User.query.get(user_id)

        if not user:
            return "Error: User could not be found."

        if len(user.created_chars) > 3:
            return "Error: You already have three Characters. You cannot create more."

        new_char = Character(char_name=character.char_name,user_id=user_id)
        db.session.add(new_char)
        db.session.commit()
        return f"{character.char_name} was successfully created."


    def delete_character(self, char_id):
        """
        Delete a char
        """
        char = Character.query.get(char_id)

        if not char:
            return "Error: Character could not be found."

        db.Session.delete(char)
        db.session.commit()
        return f" The Character {char.char_name} was successfully deleted from Database."


    def get_skills(self, skill):
        pass




