from data import data_manager


def get_shows(data):
    return data_manager.execute_select(
        "SELECT shows.id, title, year, runtime, genre, ROUND(rating, 2) AS rating, trailer, homepage "
        "FROM shows "
        "INNER JOIN (SELECT show_id, string_agg(DISTINCT genres.name, ',') AS genre "
        "FROM genres "
        "INNER JOIN (SELECT * FROM ("
        "SELECT show_id, genre_id, row_number() OVER ("
        "PARTITION BY show_id ORDER BY genre_id) AS rownum FROM show_genres) tmp "
        "WHERE rownum <= 3 ) AS sh_genres "
        "ON sh_genres.genre_id = genres.id "
        "GROUP BY 1) AS gs "
        "ON shows.id = gs.show_id "
        "ORDER BY rating DESC "
        "OFFSET (%(page_id)s-1)*%(limit)s "
        "LIMIT %(limit)s;",
        # {'header': data['header'],
        #  'order': data['order'],
        {'page_id': data['page_id'],
         'limit': data['limit']}
    )

def sorted_by_title_ASC(data):
    return data_manager.execute_select(
        "SELECT shows.id, title, year, runtime, genre, ROUND(rating, 2) AS rating, trailer, homepage "
        "FROM shows "
        "INNER JOIN (SELECT show_id, string_agg(DISTINCT genres.name, ',') AS genre "
        "FROM genres "
        "INNER JOIN (SELECT * FROM ("
        "SELECT show_id, genre_id, row_number() OVER ("
        "PARTITION BY show_id ORDER BY genre_id) AS rownum FROM show_genres) tmp "
        "WHERE rownum <= 3 ) AS sh_genres "
        "ON sh_genres.genre_id = genres.id "
        "GROUP BY 1) AS gs "
        "ON shows.id = gs.show_id "
        "ORDER BY title ASC "
        "OFFSET (%(page_id)s-1)*%(limit)s "
        "LIMIT %(limit)s;",
        # {'header': data['header'],
        #  'order': data['order'],
        {'page_id': data['page_id'],
         'limit': data['limit']}
    )


def sorted_by_title_DESC(data):
    return data_manager.execute_select(
        "SELECT shows.id, title, year, runtime, genre, ROUND(rating, 2) AS rating, trailer, homepage "
        "FROM shows "
        "INNER JOIN (SELECT show_id, string_agg(DISTINCT genres.name, ',') AS genre "
        "FROM genres "
        "INNER JOIN (SELECT * FROM ("
        "SELECT show_id, genre_id, row_number() OVER ("
        "PARTITION BY show_id ORDER BY genre_id) AS rownum FROM show_genres) tmp "
        "WHERE rownum <= 3 ) AS sh_genres "
        "ON sh_genres.genre_id = genres.id "
        "GROUP BY 1) AS gs "
        "ON shows.id = gs.show_id "
        "ORDER BY title DESC "
        "OFFSET (%(page_id)s-1)*%(limit)s "
        "LIMIT %(limit)s;",
        # {'header': data['header'],
        #  'order': data['order'],
        {'page_id': data['page_id'],
         'limit': data['limit']}
    )

def sorted_by_rating_ASC(data):
    return data_manager.execute_select(
        "SELECT shows.id, title, year, runtime, genre, ROUND(rating, 2) AS rating, trailer, homepage "
        "FROM shows "
        "INNER JOIN (SELECT show_id, string_agg(DISTINCT genres.name, ',') AS genre "
        "FROM genres "
        "INNER JOIN (SELECT * FROM ("
        "SELECT show_id, genre_id, row_number() OVER ("
        "PARTITION BY show_id ORDER BY genre_id) AS rownum FROM show_genres) tmp "
        "WHERE rownum <= 3 ) AS sh_genres "
        "ON sh_genres.genre_id = genres.id "
        "GROUP BY 1) AS gs "
        "ON shows.id = gs.show_id "
        "ORDER BY rating ASC "
        "OFFSET (%(page_id)s-1)*%(limit)s "
        "LIMIT %(limit)s;",
        # {'header': data['header'],
        #  'order': data['order'],
        {'page_id': data['page_id'],
         'limit': data['limit']}
    )

def sorted_by_rating_DESC(data):
    return data_manager.execute_select(
        "SELECT shows.id, title, year, runtime, genre, ROUND(rating, 2) AS rating, trailer, homepage "
        "FROM shows "
        "INNER JOIN (SELECT show_id, string_agg(DISTINCT genres.name, ',') AS genre "
        "FROM genres "
        "INNER JOIN (SELECT * FROM ("
        "SELECT show_id, genre_id, row_number() OVER ("
        "PARTITION BY show_id ORDER BY genre_id) AS rownum FROM show_genres) tmp "
        "WHERE rownum <= 3 ) AS sh_genres "
        "ON sh_genres.genre_id = genres.id "
        "GROUP BY 1) AS gs "
        "ON shows.id = gs.show_id "
        "ORDER BY rating DESC "
        "OFFSET (%(page_id)s-1)*%(limit)s "
        "LIMIT %(limit)s;",
        # {'header': data['header'],
        #  'order': data['order'],
        {'page_id': data['page_id'],
         'limit': data['limit']}
    )


def get_show_by_id(show_id):
    return data_manager.execute_select("SELECT shows.id, title, year, runtime, overview, genre, ROUND(rating, 2) AS rating, REPLACE(trailer, 'watch?v=', 'embed/') AS video, homepage, string_agg(DISTINCT a.name, ', ') AS actors "
        "FROM shows "
        "INNER JOIN (SELECT show_id, string_agg(DISTINCT genres.name, ',') AS genre "
        "FROM genres "
        "INNER JOIN (SELECT * FROM ("
        "SELECT show_id, genre_id, row_number() OVER ("
        "PARTITION BY show_id ORDER BY genre_id) AS rownum FROM show_genres) tmp "
        "WHERE rownum <= 3 ) AS sh_genres "
        "ON sh_genres.genre_id = genres.id "
        "GROUP BY 1) AS gs "
        "ON shows.id = gs.show_id "
        "INNER JOIN show_characters sc on shows.id = sc.show_id "
        "INNER JOIN actors a on sc.actor_id = a.id "
        "GROUP BY shows.id, gs.genre "                               
        "HAVING shows.id = %(show_id)s;",
        {'show_id': show_id}
    )


def get_seasons_by_show_id(show_id):
    return data_manager.execute_select("SELECT * FROM seasons "
                                       "WHERE show_id = %(show_id)s",
                                       {'show_id' : show_id})

def get_actors():
    return data_manager.execute_select("SELECT a.name, string_agg(DISTINCT s.title, '#') AS titles, COUNT(*) as show_numbers "
                                        "FROM actors a "
                                        "JOIN show_characters sc on a.id = sc.actor_id "
                                        "JOIN shows s on sc.show_id = s.id "
                                        "GROUP BY a.name "
                                        "ORDER BY show_numbers DESC "
                                        "LIMIT 20;")
