from flask import Flask , render_template, session , request , redirect
import random
app = Flask(__name__)
app.secret_key = "ayem"

@app.route("/")
def index():
    if "num" not in session:
        session['num'] = random.randint(1,100)
    return render_template("index.html")

@app.route("/guess" , method=['POST'])
def guess():
    session['guess'] = int(request.form['guess'])
    return redirect('/')



if __name__ == "__main__":
    app.run(debug=True)
