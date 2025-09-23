import mysql.connector

DB_NAME = 'Django_FastAPI_project'
DB_USER = 'root'
DB_PASSWORD = 'Amulya@3015'
DB_HOST = 'localhost'  # Or your DB host

def drop_all_tables():
    try:
        cnx = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        cursor = cnx.cursor()

        # Extend max length to avoid SQL truncation
        cursor.execute("SET SESSION group_concat_max_len = 1000000;")

        # Disable foreign key checks
        cursor.execute("SET FOREIGN_KEY_CHECKS = 0;")

        # Generate DROP TABLE statements for all tables
        cursor.execute(f"""
            SELECT GROUP_CONCAT(CONCAT('DROP TABLE IF EXISTS `', table_name, '`') SEPARATOR '; ')
            FROM information_schema.tables
            WHERE table_schema = '{DB_NAME}';
        """)
        result = cursor.fetchone()
        drop_statement = result[0]

        if drop_statement:
            # Execute each DROP TABLE command
            for statement in drop_statement.split(";"):
                if statement.strip():
                    cursor.execute(statement + ";")
            print("✅ All tables dropped successfully.")
        else:
            print("ℹ️ No tables found in the database.")

        # Re-enable foreign key checks
        cursor.execute("SET FOREIGN_KEY_CHECKS = 1;")

        cursor.close()
        cnx.close()

    except mysql.connector.Error as err:
        print("❌ Error:", err)

if __name__ == "__main__":
    drop_all_tables()
