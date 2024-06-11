from flask import Flask, render_template, request, redirect

app = Flask(__name__)


pokemon = {}



#! Display Route
@app.route('/')
def index():
    return render_template('index.html')


#! Action Route
@app.route('/create_pokemon', methods=['POST'])
def create_pokemon():
    name = request.form['name']
    type = request.form['type']
    generation = request.form['generation']
    pokemon_image_path = request.form['pokemon_image_path']

    pokemon[name] = {
        'name': name,
        'type': type,
        'generation': generation,
        'image_path': pokemon_image_path
    }


    return redirect('/show_pokemon/' + name)


@app.route('/show_pokemon/<name>')
def show_pokemon(name):
    pokemon_info = pokemon.get(name)
    return render_template('show_pokemon.html', pokemon_info=pokemon_info)

if __name__ == '__main__':
    app.run(debug=True)

