import unittest
from src.main import Book, PrintedBook, EBook,User,Librarian,Library

class TestBook(unittest.TestCase):
    def test_book_available_and_change_status(self):
        book = Book("Война и мир", "Толстой", 1869)
        self.assertTrue(book.is_available())
        book.mark_as_taken()
        self.assertFalse(book.is_available())
        book.mark_as_returned()
        self.assertTrue(book.is_available())

class TestPrintedBook(unittest.TestCase):
    def test_repair_improves_condition(self):
        book = PrintedBook("Преступление и наказание", "Достоевский", 1866, 480, "плохая")
        self.assertEqual(book.condition, "плохая")
        book.repair()
        self.assertEqual(book.condition, "хорошая")
        book.repair()
        self.assertEqual(book.condition, "новая")
class TestLibrary(unittest.TestCase):

    def test_lend_and_return_book(self):
        library = Library()
        user = User("Анна")
        librarian = Librarian("Мария")
        book = PrintedBook("Война и мир", "Толстой", 1869, 1225, "хорошая")
        librarian.add_book(library, book)
        librarian.register_user(library, user)
         # выдаём книгу
        library.lend_book("Война и мир", "Анна")
        self.assertFalse(book.is_available())
        self.assertIn(book, user.get_borrowed_books())

        library.return_book("Война и мир", "Анна")
        self.assertTrue(book.is_available())
        self.assertNotIn(book, user.get_borrowed_books())