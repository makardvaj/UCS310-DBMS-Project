from auth import register, login
from recommend import recommend_movies

def main():
    print("1. Register\n2. Login")
    choice = input("Select option: ")

    if choice == "1":
        username = input("Enter username: ")
        password = input("Enter password: ")
        register(username, password)
    elif choice == "2":
        username = input("Enter username: ")
        password = input("Enter password: ")
        user_id = login(username, password)
        if user_id:
            recommend_movies(user_id)

if __name__ == '__main__':
    main()
