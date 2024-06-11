from flask import Flask , render_template                             # Import Flask to allow us to create our app
app = Flask(__name__)                                                 # Create a new instance of the Flask class called "app"

@app.route('/')                                                       # The "@" decorator associates this route with the function immediately following
def hello_world():
    return render_template("index.html")                                              # Return the string 'Hello World!' as a response

if __name__=="__main__":
    app.run(debug=True)

'''''
@app.route('/succes')
def success():
    return "success"

@app.route('/hello/<name>')
def hello(name):
    print(name)
    return "hello"" " + name

@app.route('/hello/<name>/<int:num>')
def hello(name,num):
    return f"hello,{name * num}"

if __name__ == "__main__":                                        # Ensure this file is being run directly and not from a different module
    app.run(debug=True)                                           # Run the app in debug mode

    app.run(debug=True, host="localhost", port=8000)
'''''