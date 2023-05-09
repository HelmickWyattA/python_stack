from flask_app.config.mysqlconnection import connectToMySQL

class User:
    def __init__(self, info):
        self.id = info['id']
        self.first_name = info['first_name']
        self.last_name = info['last_name']
        self.email = info['email']
        self.created_at = info['created_at']

#this class method displays the entire list of users
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;" 
        results = connectToMySQL("users_schema").query_db(query)
        users = [] #blank list to append new users
        for i in results:
            users.append(cls(i))
        return users
    
#this class method will add new users to the database using the data that they submitted on '/join'
    @classmethod
    def new(cls, info):
        query = "INSERT INTO users (first_name, last_name, email) VALUES (%(first_name)s,%(last_name)s,%(email)s);"
        results = connectToMySQL("users_schema").query_db(query,info)
        return results
    
    @classmethod
    def one(cls,id):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL("users_schema").query_db(query, {"id" : id})
        return cls(results[0])
    
    @classmethod
    def update(cls, info):
        query = "UPDATE users SET first_name=%(first_name)s, last_name=%(last_name)s, email=%(email)s , updated_at=NOW() WHERE id=%(id)s;"
        return connectToMySQL("users_schema").query_db(query,info)
    
    @classmethod
    def delete(cls,info):
        query = "DELETE from users WHERE id=%(id)s"
        return connectToMySQL("users_schema").query_db(query,info)