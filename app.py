import json
import os
import random

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
packs_dir = 'static/cards'


def load_packs():
    pack_data = []
    if os.path.exists(packs_dir):
        for filename in os.listdir(packs_dir):
            if filename.endswith('.json'):
                filepath = os.path.join(packs_dir, filename)
                with open(filepath, 'r') as f:
                    data = json.load(f)
                    pack_data.append({
                        'name': data['pack_name'],
                        'description': data['pack_description'],
                        'badge': data['badge'],
                        'questions': data['questions'],
                        'population': data['questions'].__len__()
                    })
    else:
        print('The packs directory wasn\'t found in the project.')
    return pack_data


@app.route('/')
def home():
    packs = load_packs()
    return render_template('index.html', packs=packs)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/play', methods=['POST', 'GET'])
def play():
    packs = load_packs()

    if request.method == 'POST':
        selected_pack_names = request.form.getlist('packs')
        player_count = request.form.get('player_count', 1)
        cards_per_player = request.form.get('cards_per_player', 5)
        return redirect(url_for('play', packs=','.join(selected_pack_names), player_count=player_count,
                                cards_per_player=cards_per_player))

    selected_pack_names = request.args.get('packs', '').split(',')
    player_count = int(request.args.get('player_count', 1))
    cards_per_player = int(request.args.get('cards_per_player', 5))

    selected_questions = []
    for pack in packs:
        if pack['name'] in selected_pack_names:
            selected_questions += pack['questions']

    random.shuffle(selected_questions)

    return render_template('play.html', cards=selected_questions[:player_count * cards_per_player])


@app.route('/disclaimer')
def disclaimer():
    return render_template('disclaimer.html')

@app.route('/privacy_policy')
def privacy_policy():
    return render_template('privacy_policy.html')


if __name__ == '__main__':
    app.run()
