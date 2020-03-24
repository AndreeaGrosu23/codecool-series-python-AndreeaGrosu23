from data import data_manager


def get_shows(limit):
    return data_manager.execute_select(
        "SELECT title, year, runtime, genre, ROUND(rating, 2) AS rating, trailer, homepage "
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
        "ORDER BY rating DESC LIMIT %(limit)s;",
        {'limit':limit}
    )
