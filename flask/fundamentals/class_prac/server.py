from flask import Flask, render_template, request

app = Flask(__name__)
# our index route will handle rendering our form
@app.route('/')
def index():
    return render_template("index.html")

@app.route("/submit",methods=["POST"])
def submit():
    print(request.form)
    return render_template("dash.html")


@app.route("/dash")
def dashI():
    return render_template


if __name__ == "__main__":
    app.run(debug=True)

