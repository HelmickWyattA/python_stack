from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.user import User
from flask_app.models.recipe import Recipe
from . import users

@app.route('/dash')
def dash():
    if 'user_id' not in session:
        return redirect('/')
    data = {'id': session['user_id']}
    return render_template('dash.html', user = User.get_by_id(data), recipes = Recipe.get_recipes())

@app.route('/recipe/add')
def add_recipe(): 
    return render_template('new_recipe.html')

@app.route('/recipe/post', methods=["POST"])
def post_recipe():
    if 'user_id' not in session: 
        return redirect ('/')
    if not Recipe.validate_recipe(request.form):
        redirect('recipe/add')
            ### FIX THESE###
    data = {
        'name': request.form['name'],
        'description': request.form['description'],
        'instructions': request.form['instructions'],
        'under': int(request.form['under']),
        'date_made': request.form['date_made'],
        'user_id': session['user_id']
    }       ### FIX THESE###
    # print(data)
    Recipe.save_recipe(data)
    return redirect('/dash')

@app.route('/recipe/edit/<int:id>')
def edit_recipe(id):
    if 'user_id' not in session:
        return redirect('/user/login')

    return render_template('edit_recipe.html',recipe=Recipe.recipe_by_id({'id': id}))

@app.route('/recipe/edit/submit/<int:id>', methods=["POST"])
def submit_edit(id):
    if 'user_id' not in session:
        return redirect('/')
    if not Recipe.validate_recipe(request.form):
        redirect('recipe/add')

    data = {
        'id': id,
        'name': request.form['name'],
        'description': request.form['description'],
        'instructions': request.form['instructions'],
        'under': int(request.form['under']),
        'date_made': request.form['date_made'],
    }
    Recipe.update(data)
    return redirect('/dash')

@app.route('/recipe/view/<int:id>')
def view(id):
    if 'user_id' not in session:
        return redirect('/')

    return render_template('view.html',recipe=Recipe.recipe_by_id({'id': id}))

@app.route('/recipe/delete/<int:id>')
def delete(id):
    if 'user_id' not in session:
        return redirect('/')

    Recipe.delete({'id':id})
    return redirect('/dash')