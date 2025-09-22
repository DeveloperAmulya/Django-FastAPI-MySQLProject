import mysql.connector

from mysql.connector import errorcode

DB_NAME = "Django_FastAPI_project"
DB_USER = "root"
DB_PASSWORD="Amulya@3015"
DB_HOST="localhost"
NEW_USER = "fastuser"
NEW_PASS="Amulya@3015" 

def create_database():
    try:
        #connect to mysql server(not a secific DB)
        cnx = mysql.connector.connect(user=DB_USER, password = DB_PASSWORD, host=DB_HOST)
        cursor = cnx.cursor()
        cursor.execute(
            f"CREATE DATABASE IF NOT EXISTS {DB_NAME} CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;"
        )
        print(f"Database '{DB_NAME}' created or already exists.")
# Optional: create a dedicated user with privileges
        try:
            cursor.execute(
                f"CREATE USER '{NEW_USER}'@'localhost' IDENTIFIED BY '{NEW_PASS}';"
            )
            print(f" User '{NEW_USER}' created.")
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_CANNOT_USER:
                print(f" User '{NEW_USER}' may already exist, skipping.")
            else:
                raise

        cursor.execute(
            f"GRANT ALL PRIVILEGES ON {DB_NAME}.* TO '{NEW_USER}'@'localhost';"
        )
        cursor.execute("FLUSH PRIVILEGES;")
        print(f"✅ Privileges granted to '{NEW_USER}'.")
        
        cursor.close()
        cnx.close()
    except mysql.connector.Error as err:
        print(f" Error: {err}")

if __name__ == "__main__":
    create_database()