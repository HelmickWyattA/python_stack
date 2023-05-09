from flask import Flask, render_template, session, redirect

app = Flask(__name__)


app.secret_key = "gr8est c0unter 3ver"

@app.route('/')
def index():
    if "visit" in session:
        session["visit"] += 1
    else:
        session["visit"] = 0
    return render_template("index.html")

@app.route('/count')
def increment():
    if "counter" not in session:
        session["counter"] = 1
    else:
        session["counter"] += 1
    return render_template("index.html")

@app.route('/plustwo')
def addtwo():
    session["counter"] += 2
    return render_template("index.html")
    
@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)