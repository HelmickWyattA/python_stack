from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask import flash, request
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
import re


EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    db = "recipes_db"
    def __init__(self,data):
        self.id =data['id']
        self.first_name =data['first_name']
        self.last_name =data['last_name']
        self.email =data['email']
        self.password =data['password']
        self.created_at =data['created_at']
        self.updated_at =data['updated_at']
        self.recipes = []
    
    @classmethod
    def save(cls,data):
        query = "INSERT INTO users (first_name,last_name,email,password) VALUES(%(first_name)s,%(last_name)s,%(email)s,%(password)s);"
        return connectToMySQL(cls.db).query_db(query,data)
    
    @staticmethod
    def validate_registration(user):
        is_valid = True
        if len(user['first_name']) < 3:
            flash("Invalid: First name must contain AT LEAST 3 characters","registration")
            is_valid = False
        if len(user['last_name']) < 3:
            flash("Invalid: Last name must contain AT LEAST 3 characters","registration")
            is_valid = False
        if len(user['email']) < 1:
            flash("Must enter an email address","registration")
            is_valid = False
        elif not EMAIL_REGEX.match(user['email']):
            flash("A user with that email address already exists","registration")
            is_valid = False
        if len(user['password']) < 8:
            flash("Invalid: Password must contain AT LEAST 8 characters","registration")
            is_valid = False
        if user['password'] != user['confirm']:
            flash("Invalid: 'Password' field must match 'Confirm Password' field","registration")
            is_valid = False
        return is_valid
    



    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(cls.db).query_db(query)
        users = []
        for row in results:
            users.append( cls(row))
        return users


    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query,data)
        if not results:
            return False
        return cls(results[0])

    @classmethod
    def get_by_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL(cls.db).query_db(query,data)
        if len(result) < 1:
            return False
        return cls(result[0])
    
    @staticmethod
    def validate_login(user):
        is_valid=True
        if not EMAIL_REGEX.match(user['email']):
            flash("Invalid Login Credentials", "login")
            return False
        user_id = User.get_by_email(user)
        if not user_id:
            flash("Invalid Login Credentials", "login")
            return False
        if not bcrypt.check_password_hash(user_id.password, request.form['password']):
            flash("Invalid Login Credentials", "login")
            return False
        return is_valid