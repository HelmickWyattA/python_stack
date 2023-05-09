from flask import Flask, render_template


app = Flask(__name__)

# displays 3 blue boxes
@app.route("/play")
def first_play():
    return render_template("index.html",num=3, color="blue")

# choose your amount of blue boxes
@app.route("/play/<int:num>")
def second_play(num):
    return render_template("index.html", num=num, color="blue")

#choose the color AND the amount of boxes
@app.route("/play/<int:num>/<string:color>")
def third_play(num, color):
    return render_template("index.html", num=num, color=color)


if __name__=="__main__":
    app.run(debug=True)