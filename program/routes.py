from program import app
from flask import render_template
import requests


@app.route('/test/api')
def test_api() -> str:
    return 'Hello Pythonista!'

@app.route('/api/joke')
def get_chuck_norris_joke() -> str:
    joke = get_chuck_api()

    return render_template('index.html', joke=joke)



def get_chuck_api() -> str:
    r = requests.get('https://api.chucknorris.io/jokes/random')
    result = r.json()

    return result['value']

