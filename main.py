from flask import Flask, render_template, request, redirect, url_for, session, json, jsonify
from data import queries

import os

app = Flask('codecool_series')

app.secret_key = os.urandom(8)

@app.route('/')
def index():
    page_id = 1
    data = {
        'limit': 15,
        'page_id': 1
    }
    shows = queries.get_shows(data)
    if session:
        username = session['username']
        faves = queries.select_fav(username)
        shows = queries.get_shows(data)
        header = request.args.get(key = 'header')
        order = request.args.get(key = 'order')
        if header == "title" and order == "asc" :
            shows = queries.sorted_by_title_ASC(data)
        elif header == "title" and order == "desc" :
            shows = queries.sorted_by_title_DESC(data)
        elif header == "rating" and order == "asc" :
            shows = queries.sorted_by_rating_ASC(data)
        elif header == "rating" and order == "desc" :
            shows = queries.sorted_by_rating_DESC(data)
        return render_template('index.html', shows=shows, page_id=page_id, username=username, faves=faves)

    return render_template('index.html', shows=shows, page_id=page_id)

    # if session:
    #     shows = queries.sorted_by_rating_DESC(data)
    #     username = session['username']
    #     faves = queries.select_fav(username)
    #     return render_template('index.html', shows=shows, page_id=page_id, username=username, faves=faves)




@app.route('/get-shows')
def get_shows():
    queries.get_shows()


@app.route('/get-shows/<page_id>')
def get_shows_per_page(page_id):
    data = {
        'limit': 15,
        'page_id': page_id
    }
    try:
        shows = queries.get_shows(data)
        return render_template('index.html', shows=shows, page_id=int(page_id))
    except:
        page_id = 0
        data = {
            'limit': 15,
            'page_id': 1
        }
        shows = queries.get_shows(data)
        return render_template('index.html', shows=shows, page_id=int(page_id))


@app.route('/tv-show')
@app.route('/tv-show/<show_id>')
def show_details(show_id):
    show = queries.get_show_by_id(show_id)
    seasons = queries.get_seasons_by_show_id(show_id)
    return render_template('show_details.html', show=show, seasons=seasons)


@app.route('/top-20-actors')
def top_20():
    actors = queries.get_actors()
    return render_template('top20actors.html', actors=actors)


@app.route('/design')
def design():
    return render_template('design.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        session['username'] = request.form['username']
        return redirect(url_for('index'))
#     to write function for checking in the username exists and password is correct


@app.route('/add-favorite')
def add_fav():
    data = {
        'show_id': request.args.get(key='show_id'),
        'username': request.args.get(key='username'),
    }
    queries.add_fav_to_users(data)
    return redirect(url_for('index'))


@app.route('/api/tv-show/<season_id>')
def get_episodes(season_id):
    episodes = queries.get_episodes(season_id)
    return jsonify(episodes)

# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     to write function to write in database
#     to generate db table with users
#     to write hash password


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
