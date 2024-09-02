import sqlite3
con = sqlite3.connect('movie.db')
koorsor = con.cursor()
koorsor.execute('''SELECT title, genre
FROM movies
INNER JOIN movies_genres ON movies.id = movies_genres.movie_id
INNER JOIN genres ON movies_genres.genre_id = genres.genre_id ''')
result = koorsor.fetchall()
con.close()
for i in result:
    print(i)
