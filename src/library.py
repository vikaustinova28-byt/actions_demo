class Book:
    def __init__(self, title, author, year):
        self.__title = title
        self.__author = author
        self.__year = year
        self.__available = True

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_year(self):
        return self.__year

    def is_available(self):
        return self.__available

    def mark_as_taken(self):
        self.__available = False

    def mark_as_returned(self):
        self.__available = True

    def __str__(self):
        status = "доступна" if self.__available else "недоступна"
        return f"'{self.__title} - {self.__author}, {self.__year} ({status})"


class PrintedBook(Book):
    def __init__(self, title, author, year, pages, condition="новая"):
        super().__init__(title, author, year)
        self.pages = pages
        self.condition = condition

    def repair(self):
        if self.condition == "плохая":
            self.condition = "хорошая"
        elif self.condition == "хорошая":
            self.condition = "новая"
        print(f"Книга «{self.get_title()}» отремонтирована, состояние: {self.condition}")

    def __str__(self):
        return f"{super().__str__()} — {self.pages} стр., состояние: {self.condition}"


class EBook(Book):
    def __init__(self, title, author, year, file_size, format_):
        super().__init__(title, author, year)
        self.file_size = file_size
        self.format = format_

    def download(self):
        print(f"Книга «{self.get_title()}» загружается...")

    def __str__(self):
        return f"{super().__str__()} — {self.file_size}MB, формат: {self.format}"


class User:
    def __init__(self, name):
        self.name = name
        self.__borrowed_books = []

    def borrow(self, book):
        if book.is_available():
            book.mark_as_taken()
            self.__borrowed_books.append(book)
            print(f"{self.name} взял(а) книгу «{book.get_title()}».")
        else:
            print(f"Книга «{book.get_title()}» недоступна.")

    def return_book(self, book):
        if book in self.__borrowed_books:
            book.mark_as_returned()
            self.__borrowed_books.remove(book)
            print(f"{self.name} вернул(а) книгу «{book.get_title()}».")
        else:
            print(f"{self.name} не имеет книгу «{book.get_title()}» у себя.")

    def show_books(self):
        if not self.__borrowed_books:
            print(f"{self.name} не взял(а) ни одной книги.")
        else:
            print(f"Книги у {self.name}:")
            for b in self.__borrowed_books:
                print("  -", b)

    def get_borrowed_books(self):
        return tuple(self.__borrowed_books)


class Librarian(User):
    def add_book(self, library, book):
        library.add_book(book)
        print(f"{self.name} добавил(а) книгу «{book.get_title()}» в библиотеку.")

    def remove_book(self, library, title):
        library.remove_book(title)
        print(f"{self.name} удалил(а) книгу «{title}» из библиотеки.")

    def register_user(self, library, user):
        library.add_user(user)
        print(f"{self.name} зарегистрировал(а) пользователя: {user.name}")


class Library:
    def __init__(self):
        self.__books = []
        self.__users = []

    def add_book(self, book):
        self.__books.append(book)

    def remove_book(self, title):
        for b in self.__books:
            if b.get_title() == title:
                self.__books.remove(b)
                break

    def add_user(self, user):
        self.__users.append(user)

    def find_book(self, title):
        for b in self.__books:
            if b.get_title() == title:
                return b
        return None

    def show_all_books(self):
        print("Все книги:")
        for b in self.__books:
            print("  -", b)

    def show_available_books(self):
        print("Доступные книги:")
        for b in self.__books:
            if b.is_available():
                print("  -", b)

    def lend_book(self, title, user_name):
        book = self.find_book(title)
        user = next((u for u in self.__users if u.name == user_name), None)
        if book and user:
            user.borrow(book)
        else:
            print("Ошибка: книга или пользователь не найдены.")

    def return_book(self, title, user_name):
        book = self.find_book(title)
        user = next((u for u in self.__users if u.name == user_name), None)
        if book and user:
            user.return_book(book)
        else:
            print("Ошибка: книга или пользователь не найдены.")


if __name__ == '__main__':
    lib = Library()

    # --- создаём книги ---
    b1 = PrintedBook("Война и мир", "Толстой", 1869, 1225, "хорошая")
    b2 = EBook("Мастер и Маргарита", "Булгаков", 1966, 5, "epub")
    b3 = PrintedBook("Преступление и наказание", "Достоевский", 1866, 480,
                     "плохая")

    # --- создаём пользователей ---
    user1 = User("Анна")
    librarian = Librarian("Мария")

    # --- библиотекарь добавляет книги ---
    librarian.add_book(lib, b1)
    librarian.add_book(lib, b2)
    librarian.add_book(lib, b3)

    # --- библиотекарь регистрирует пользователя ---
    librarian.register_user(lib, user1)

    # --- пользователь берёт книгу ---
    lib.lend_book("Война и мир", "Анна")

    user1.show_books()

    lib.return_book("Война и мир", "Анна")

    b2.download()

    b3.repair()
    print(b3)

