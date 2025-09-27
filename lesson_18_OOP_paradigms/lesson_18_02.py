"""
_ - защищенный
__ - приватный
"""


class Book:

    def __init__(self, title, author, year=None):
        self._title = title
        self._author = author
        if not year:
            self._year = 'не указано'
        else:
            self._year = year


if __name__ == '__main__':
    book = Book("Дубровский", "Пушкин А.C.")
    print(book._title)
    print(book._author)
    print(book._year)
    print()

    book._title = "Странный Человек"
    book._author = 'Лермонтов М.Ю.'
    print(book._title)
    print(book._author)
