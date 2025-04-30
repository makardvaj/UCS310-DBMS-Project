import mysql.connector
from auth import connect_db

def recommend_movies(user_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT genre FROM movies m
        JOIN ratings r ON m.movie_id = r.movie_id
        WHERE r.user_id = %s
        GROUP BY genre
        ORDER BY COUNT(*) DESC
        LIMIT 1
    """, (user_id,))
    result = cursor.fetchone()
    genre = result[0] if result else None

    if genre:
        print(f"Recommended movies in your favorite genre ({genre}):")
        cursor.execute("SELECT title FROM movies WHERE genre=%s ORDER BY rating DESC LIMIT 5", (genre,))
    else:
        print("Top-rated movies:")
        cursor.execute("SELECT title FROM movies ORDER BY rating DESC LIMIT 5")

    for (title,) in cursor.fetchall():
        print("-", title)
    conn.close()
