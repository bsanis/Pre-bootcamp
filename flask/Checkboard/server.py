from flask import Flask, render_template
app = Flask(__name__)

@app.route('/<int:x>/<int:y>/<string:color_one>/<string:color_two>')
def row_col(x,y,color_one,color_two):
    return render_template("index.html",row=x,col=y,color_one=color_one,color_two=color_two)



if __name__ == "__main__":
    app.run(debug=True)