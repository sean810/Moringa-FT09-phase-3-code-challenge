import sqlite3

def create_tables():
    # Connect to the database
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Create the authors table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS authors (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    )
    ''')

    # Create the magazines table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS magazines (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        category TEXT NOT NULL
    )
    ''')

    # Create the articles table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS articles (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        author_id INTEGER NOT NULL,
        magazine_id INTEGER NOT NULL,
        FOREIGN KEY (author_id) REFERENCES authors (id),
        FOREIGN KEY (magazine_id) REFERENCES magazines (id)
    )
    ''')

    # Commit changes and close the connection
    conn.commit()
    conn.close()
