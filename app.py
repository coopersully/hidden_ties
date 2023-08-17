import json
import random

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/play')
def play():
    with open('static/cards/normal.json') as file:
        cards = json.load(file)
        random.shuffle(cards)
        return render_template('play.html', cards=cards)


if __name__ == '__main__':
    app.run()
