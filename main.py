from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
from data import queries, data_manager

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
        user_id = session['user_id']
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


        faves = queries.select_fav(user_id)
        if faves:
            return render_template('index.html', shows=shows, page_id=page_id, faves=faves)

        return render_template('index.html', shows=shows, page_id=page_id)

    return render_template('index.html', shows=shows, page_id=page_id)


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
    comments = queries.show_comment()
    return render_template('show_details.html', show=show, seasons=seasons, comments=comments)


@app.route('/top-20-actors')
def top_20():
    actors = queries.get_actors()
    return render_template('top20actors.html', actors=actors)


@app.route('/add-favorite')
def add_fav():
    user_id = session['user_id']
    show_id = request.args.get(key='show_id')
    data = {
        'show_id': show_id,
        'user_id': user_id
    }
    queries.add_fav_to_users(data)
    return redirect(url_for('index'))


@app.route('/design')
def design():
    return render_template('design.html')


# @app.route('/api/add-favorite', methods=['POST'])
# def add_fav():
#     user_id = session['user_id']
#     show_id = request.json['show_id']
#     data = {
#         'show_id': show_id,
#         'user_id': user_id
#     }
#     queries.add_fav_to_users(data)
#     return redirect(url_for('index'))


@app.route('/api/tv-show/<season_id>')
def get_episodes(season_id):
    episodes = queries.get_episodes(season_id)
    return jsonify(episodes)


@app.route('/add-comment/<show_id>', methods=['GET', 'POST'])
def write_comment(show_id):
    if request.method=='POST':
        user_id = session['user_id']
        comment_text = request.form['comment']
        data = {
            'show_id': show_id,
            'user_id': user_id,
            'comment_text': comment_text
        }
        queries.add_comment(data)
    return redirect(url_for('show_details', show_id=show_id))



@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        if request.form['password1'] == request.form['password2']:
            form_data = {
                'username': request.form['username'],
                'hashed_pass': data_manager.hash_password(request.form['password1']),
                'user_email': request.form['email-address']
            }
            queries.add_user(form_data)
            return redirect(url_for('index'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'logged_in' in session:
        return redirect(url_for('index'))

    if request.method == "POST":
        input_password = request.form['password']
        db_pass = queries.login(request.form['username'])
        if data_manager.verify_password(input_password, db_pass[0]):
            username = request.form['username']
            user_id = queries.user_id_by_username(username)
            session['user_id'] = user_id
            session['username'] = request.form['username']
            return redirect(url_for('index'))
        else:
            flash('Password does not match')
    return redirect(url_for('index'))


@app.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('user_id', None)
    return redirect(url_for('index'))


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
