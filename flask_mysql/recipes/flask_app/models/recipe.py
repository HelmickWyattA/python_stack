from flask import session, flash
from flask_app.models.user import User
from flask_app.config.mysqlconnection import connectToMySQL


class Recipe:

    db = "recipes_db"

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.date_made = data['date_made']
        self.under = data['under']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.creator = None


    @classmethod
    def save_recipe(cls,data):
        query = "INSERT INTO recipes(name, description, instructions, date_made, under, user_id) VALUES(%(name)s, %(description)s, %(instructions)s, %(date_made)s, %(under)s,%(user_id)s);"
        return connectToMySQL(cls.db).query_db(query,data)
    
    @classmethod
    def get_recipes(cls):
        query = "SELECT * FROM recipes JOIN users on recipes.user_id = users.id;"
        results = connectToMySQL(cls.db).query_db(query)
        recipes = []
        for data in results: 
            recipe = cls(data)
            data = {
                'id':data['users.id'],
                'first_name': data['first_name'],
                'last_name': data['last_name'],
                'email': data['email'],
                'password': ' ',
                'created_at': data['users.created_at'],
                'updated_at': data['users.created_at']
            }
            recipe.creator = User(data)
            recipes.append(recipe)
        return recipes
    
    @classmethod
    def recipe_by_id(cls,data):
        query = "SELECT * FROM recipes JOIN users on recipes.user_id = users.id WHERE recipes.id = %(id)s;"
        result = connectToMySQL(cls.db).query_db(query,data)
        if not result:
            return False
        result = result[0]
        recipe = cls(result)
        user = {
            'id':result['users.id'],
            'first_name': result['first_name'],
            'last_name': result['last_name'],
            'email': result['email'],
            'password': ' ',
            'created_at': result['users.created_at'],
            'updated_at': result['users.created_at']
        }
        recipe.creator = User(user)
        return recipe

    @classmethod
    def update(cls, data):
        query = "UPDATE recipes SET name=%(name)s, description=%(description)s, instructions=%(instructions)s, under=%(under)s, date_made=%(date_made)s,updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query,data)
    
    @classmethod
    def delete(cls,data):
        query = "DELETE FROM recipes WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query,data)
    ### FIX THESE###
    @staticmethod
    def validate_recipe(data):
        is_valid = True
        if len(data['name']) < 3:
            flash("Recipe Name must be AT LEAST 3 characters long", "recipe")
            is_valid = False
        if len(data['description']) < 3:
            flash("Recipe description must be AT LEAST 3 characters long", "recipe")
            is_valid = False
        if len(data['instructions']) < 3:
            flash("Recipe instructions must be AT LEAST 3 characters long", "recipe")
            is_valid = False
        if 'under' not in data:
            flash("Please select yes or no", "recipe")
            is_valid = False
        if data['date_made'] == " ":
            flash("Please select a date", "recipe")
            is_valid = False
        return is_valid
    ### FIX THESE ###