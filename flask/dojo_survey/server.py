from flask import Flask, render_template, session, redirect, request

app = Flask(__name__)


app.secret_key = "0s1u2r3v4e5y"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/result', methods=['POST'])
def results():
    print("Got Post Info")
    session['username'] = request.form['name']
    session['userlocation'] = request.form['location']
    session ['userlanguage'] = request.form['language']
    session ['usercomments'] = request.form['comment']
    return render_template("result.html")

    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)