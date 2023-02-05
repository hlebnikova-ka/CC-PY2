class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self.name = name
        self.author = author

    @property
    def name(self) -> str:
        return self.name

    @property
    def author(self) -> str:
        return self.author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    @property
    def pages(self) -> int:
        return self._pages

    @pages.setter
    def pages(self, new_pages) -> None:

        if not  isinstance(new_pages, int):
            raise TypeError("Кол-во страниц должно быть  типа int")
        if new_pages <= 0:
            raise TypeError("Кол-во страниц должно быть положительным числом")
        self._pages = new_pages

    def __repr__(self):  # перезагружаем rep т.к. добавляется аргумент pages
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self._pages!r})"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    @property
    def duration(self) -> str:
        return self._duration

    @duration.setter
    def duration(self, new_duration) -> None:

        if not isinstance(new_duration, float):
            raise TypeError("Длительность должна быть типа float")
        if new_duration <= 0:
            raise ValueError("Длительность должна быть положительным числом")
        self.duration = new_duration

    def __repr__(self):  # перезагружаем rep т.к. добавляется аргумент duration
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration!r})"
