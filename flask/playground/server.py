from flask import Flask, render_template
app = Flask(__name__)


@app.route("/play")
def play_1():
    return render_template("play.html",nb=3,color="blue")

@app.route("/play/<int:nb>")
def play_2(nb):
    return render_template("play.html",nb=nb,color="blue")


@app.route("/play/<int:nb>/<string:color>")
def play_3(nb,color):
    return render_template("play.html",nb=nb,color=color)




if __name__=="__main__":
    app.run(debug=True)