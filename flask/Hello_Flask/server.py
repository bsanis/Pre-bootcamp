from flask import Flask , render_template                             # Import Flask to allow us to create our app
app = Flask(__name__)                                                 # Create a new instance of the Flask class called "app"

@app.route('/')                                                       # The "@" decorator associates this route with the function immediately following
def hello_world():
    return render_template("index.html")                                              # Return the string 'Hello World!' as a response

if __name__=="__main__":
    app.run(debug=True)

@app.route('/hello/<name>/<int:num>')
def hello(name,num):
    return render_template("hello.html",name=name,num=num)