from database.database_interface import get_all_users, create_database

def print_all_users():
    for user in get_all_users():
        print(user)

if __name__ == "__main__":
    print_all_users()