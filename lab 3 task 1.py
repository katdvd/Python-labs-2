class Book:
    """ Базовый класс книги. """

    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value):
        if not isinstance(value, int):
            raise TypeError("Количество страниц должно быть целым числом.")
        if value <= 0:
            raise ValueError("Количество страниц должно быть положительным числом.")
        self._pages = value

    def __str__(self):
         return f"{super().__str__()} , страниц: {self.pages}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages})"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Продолжительность должна быть числом.")
        if value <= 0:
            raise ValueError("Продолжительность должна быть положительной.")
        self._duration = value


    def __str__(self):
        return f"{super().__str__()} , продолжительность: {self.duration}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration})"

if __name__ == '__main__':
    book = Book("Мастер и Маргарита", "М. Булгаков")
    print(book)
    print(repr(book))
    #book.name = "Измененное название" # AttributeError: can't set attribute
    #book.author = "Другой Автор" # AttributeError: can't set attribute

    paper_book = PaperBook("Мертвые души", "Н. Гоголь", 400)
    print(paper_book)
    print(repr(paper_book))
    #paper_book.pages = "abc"  # TypeError: Количество страниц должно быть целым числом.
    #paper_book.pages = -10 # ValueError: Количество страниц должно быть положительным числом.

    audio_book = AudioBook("Евгений Онегин", "А. Пушкин", 4.5)
    print(audio_book)
    print(repr(audio_book))
    #audio_book.duration = "abc" # TypeError: Продолжительность должна быть числом.
    #audio_book.duration = -5 # ValueError: Продолжительность должна быть положительной.

    paper_book.pages = 500
    print(paper_book)

    audio_book.duration = 5.0
    print(audio_book)