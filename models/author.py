import sqlite3

class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Name must be a non-empty string.")
        
        self._name = name

        # Insert the author into the database
        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()
        cursor.execute("INSERT INTO authors (name) VALUES (?)", (self._name,))
        self._id = cursor.lastrowid
        connection.commit()
        connection.close()

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @staticmethod
    def find_by_id(author_id):
        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM authors WHERE id = ?", (author_id,))
        row = cursor.fetchone()
        connection.close()

        if row:
            return Author(row[1])
        return None

    def articles(self):
        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM articles WHERE author_id = ?", (self._id,))
        articles = cursor.fetchall()
        connection.close()
        return articles

    def magazines(self):
        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()
        cursor.execute('''
        SELECT magazines.* FROM magazines
        JOIN articles ON magazines.id = articles.magazine_id
        WHERE articles.author_id = ?
        ''', (self._id,))
        magazines = cursor.fetchall()
        connection.close()
        return magazines
