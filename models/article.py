import sqlite3
from models.author import Author  # Already added
from models.magazine import Magazine  # Add this import statement

class Article:
    def __init__(self, author, magazine, title):
        if not isinstance(title, str) or not 5 <= len(title) <= 50:
            raise ValueError("Title must be a string between 5 and 50 characters.")
        
        self._title = title
        self._author_id = author.id
        self._magazine_id = magazine.id

        # Insert the article into the database
        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO articles (title, author_id, magazine_id) VALUES (?, ?, ?)",
            (self._title, self._author_id, self._magazine_id)
        )
        self._id = cursor.lastrowid
        connection.commit()
        connection.close()

    @property
    def id(self):
        return self._id

    @property
    def title(self):
        return self._title

    def author(self):
        return Author.find_by_id(self._author_id)  # Now works since Author is imported

    def magazine(self):
        return Magazine.find_by_id(self._magazine_id)  # Now works since Magazine is imported
