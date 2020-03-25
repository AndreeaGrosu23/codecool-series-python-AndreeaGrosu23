from data import data_manager


def get_shows(data):
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
        "ORDER BY rating DESC "
        "OFFSET (%s-1)*15 "
        "LIMIT %s;",
        (data['page_id'],
         data['limit'])
    )

def get_shows_per_page(page):
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
        "ORDER BY rating DESC "
        "OFFSET (%(page)s-1)*15"
        "LIMIT 15;",
        {"page": page}
    )