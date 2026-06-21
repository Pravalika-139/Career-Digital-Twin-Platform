import sqlite3

def create_database():
    connection = sqlite3.connect("career.db")
    cursor = connection.cursor()

    # Users table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT,
        skills TEXT
    )
    """)

    # Resume Results table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS resume_results(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_name TEXT,
        detected_skills TEXT,
        score INTEGER
    )
    """)

    connection.commit()
    connection.close()

create_database()

# Delete old resume results (temporary)
connection = sqlite3.connect("career.db")
cursor = connection.cursor()

cursor.execute("DELETE FROM resume_results")

connection.commit()
connection.close()

print("Old resume results deleted")