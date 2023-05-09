from flask_app import app
from flask import render_template,redirect,request
from flask_app.models.user import User


@app.route('/')  
def index():
    return redirect('/users')

@app.route('/users')
def users():
    return render_template("all_users.html", users=User.get_all())

#this app.route will take potential users to a new page that will allow them to submit their own information to the users database
@app.route('/join')
def join():
    return render_template("add_user.html")

#this app.route adds the user info that was submitted and redirects to the main page ('/users/)
@app.route('/newuser',methods = ['POST'])
def newuser():
    print(request.form)
    User.new(request.form)
    return redirect('/users')

#READ
@app.route('/users/show/<int:id>')  
def show(id):
    user=User.one(id)
    return render_template("show_user.html", user=user)

@app.route('/users/edit/<int:id>')
def edit(id):
    user=User.one(id)
    return render_template("edit_user.html", user=user)

#UPDATE
@app.route('/users/update',methods=['POST'])
def update():
    User.update(request.form)
    return redirect('/users')

#DELETE
@app.route('/users/delete/<int:id>')
def delete(id):
    info = {"id":id}
    User.delete(info)
    return redirect('/users')
