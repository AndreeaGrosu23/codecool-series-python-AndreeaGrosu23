from flask import Flask, render_template, url_for, request
from data import queries

app = Flask('codecool_series')


@app.route('/')
def index():
    page_id = 1
    data = {
        'limit': 15,
        'page_id': 1
    }
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


@app.route('/design')
def design():
    return render_template('design.html')


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
