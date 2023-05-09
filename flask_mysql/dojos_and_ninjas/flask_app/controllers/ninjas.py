from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route('/ninjas')
def ninjas():
    dojos = Dojo.get_all()
    return render_template("ninja.html", dojos = dojos)

@app.route('/newninja', methods=['POST'])
def new_ninja():
    Ninja.save_ninja(request.form)
    return redirect('/')