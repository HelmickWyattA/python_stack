from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.dojo import Dojo

@app.route('/dojos')
def show_all():
    dojos = Dojo.get_all()
    return render_template("index.html",dojos = dojos)

@app.route('/')
def index():
    return redirect('/dojos')

@app.route('/newdojo', methods=['POST'])
def new_dojo():
    Dojo.save_dojo(request.form)
    return redirect('/')

@app.route('/showdojo/<int:id>')
def show(id):
    data = {"id": id}
    return render_template("dojo.html",dojo=Dojo.get_with_dojo_id(data))