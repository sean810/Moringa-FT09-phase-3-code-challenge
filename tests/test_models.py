import unittest
from models.author import Author
from models.article import Article
from models.magazine import Magazine

class TestModels(unittest.TestCase):
    def test_author_creation(self):
        # Create an author instance with a name
        author = Author("John Doe")
        self.assertEqual(author.name, "John Doe")

    def test_article_creation(self):
        # Create an author and a magazine instance
        author = Author("John Doe")
        magazine = Magazine("Tech Weekly", "Lifestyle")
        
        # Create an article with author and magazine instances
        article = Article(author, magazine, "Test Title")
        
        self.assertEqual(article.title, "Test Title")
        self.assertEqual(article.author().name, "John Doe")  # Check the author's name
        self.assertEqual(article.magazine().name, "Tech Weekly")  # Check the magazine's name

    def test_magazine_creation(self):
        # Create a magazine instance
        magazine = Magazine("Tech Weekly", "Lifestyle")
        self.assertEqual(magazine.name, "Tech Weekly")
        self.assertEqual(magazine.category, "Lifestyle")

if __name__ == "__main__":
    unittest.main()
