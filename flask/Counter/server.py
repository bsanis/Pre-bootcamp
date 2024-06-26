from flask import Flask , render_template , redirect , session
app = Flask(__name__)
app.secret_key = " secret "

@app.route('/')
def index():
    if "counter" not in session:
        session["counter"] = 0
    return render_template("index.html")


@app.route('/add')
def add():
    session["counter"] +=1
    return redirect("/")

@app.route('/reset')
def reset():
    session.clear()
    return redirect("/")


if __name__=="__main__":
    app.run(debug=True)