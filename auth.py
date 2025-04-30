import mysql.connector

def connect_db():
    return mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "your_password",
        database = "movie_recommendation"
    )

def register(username, password):
    conn = connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO user (username, password) VALUES (%s, %s)", (username, password))
        conn.commit()
        print("Registration successful!")
    except mysql.connector.Error as err:
        print("Error : ", err)
    finally:
        conn.close()

def login(username, password):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
    user = cursor.fetchone()
    conn.close()
    if user:    # non-nully value
        print("Login successfull!")
        return user[0]  # user_id
    else:
        print("Invalid credentials!")
        return None
