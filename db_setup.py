import mysql.connector

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "your_password" # replace this with the actual MySQL password
)

cursor = conn.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS movies_recommendation")
cursor.execute("USE movies_recommendation")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        user_id INT AUTO_INCREAMENT PRIMARY KEY,
        username VARCHAR(50) UNIQUE NOT NULL,
        password VARCHAR(100) NOT NULL
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS movies (
        movie_id INT AUTO_INCREAMENT PRIMARY KEY,
        title VARCHAR(100),
        genre VARCHER(50),
        year INT,
        rating FLOAT
    ) 
""")

cursor.execute("""
    CRAETE TABLE IF NOT EXISTS ratings (
        rating_id INT AUTO_INCREAMENT PRIMARY KEY,
        user_id INT,
        movie_id INT,
        user_rating INT,
        FOREIGN KEY (user_id) REFERENCES users(user_id),
        FOREIGN KEY (movie_is) REFERENCES movies(movie_id)
    )
""")

print("Databse and tables created.")
conn.commit()
conn.close()
