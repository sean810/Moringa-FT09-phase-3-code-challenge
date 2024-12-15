import sqlite3

class Magazine:
    def __init__(self, name, category):
        if not isinstance(name, str) or not 2 <= len(name) <= 16:
            raise ValueError("Name must be a string between 2 and 16 characters.")
        if not isinstance(category, str) or len(category) == 0:
            raise ValueError("Category must be a non-empty string.")

        self._name = name
        self._category = category

        # Insert the magazine into the database
        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()
        cursor.execute("INSERT INTO magazines (name, category) VALUES (?, ?)", (self._name, self._category))
        self._id = cursor.lastrowid
        connection.commit()
        connection.close()

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def category(self):
        return self._category

    @staticmethod
    def find_by_id(magazine_id):
        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM magazines WHERE id = ?", (magazine_id,))
        row = cursor.fetchone()
        connection.close()

        if row:
            return Magazine(row[1], row[2])
        return None

    def articles(self):
        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM articles WHERE magazine_id = ?", (self._id,))
        articles = cursor.fetchall()
        connection.close()
        return articles

    def contributors(self):
        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()
        cursor.execute('''
        SELECT DISTINCT authors.* FROM authors
        JOIN articles ON authors.id = articles.author_id
        WHERE articles.magazine_id = ?
        ''', (self._id,))
        contributors = cursor.fetchall()
        connection.close()
        return contributors
