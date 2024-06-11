from flask import Flask
app = Flask(__name__)

@app.route('/')
def Hello_world():
    return "Hello world !"

@app.route('/dojo')
def Hello_world():
    return "Dojo!"

@app.route('/say/<str:name>')
def hello(name):
    if type(name) == str:
        print(name)
        return "HI" " " + name
    else:
        print("sorry!No response. Try again")

@app.route('/repeat/<int:num>/<str:name>')
def hello(num,name):
    if type(name)==str and type(num)==int:
            return f"hello,{name * num}"
    else:
         print("sorry!No response. Try again")

