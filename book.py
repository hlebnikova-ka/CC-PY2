BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


class Book:
    def __init__(self, _id: int, name: str, pages: int):
        """
        Создание и подготовка к работе объекта "Книга"
        :param _id: Идентификатор книги
        :param name: Название книги
        :param pages: Кол-во страниц в книге
        """
        if not isinstance(_id, int):
            raise TypeError("Введите целое число в поле id")
        self._id = _id

        if not isinstance(name, str):
            raise TypeError("Введите строковое назвние в поле name")
        self.name = name

        if not isinstance(pages, int):
            raise TypeError("Введите целое число в поле pages")
        self.pages = pages

    def __str__(self) -> str:
        return f'Книга"{self.name}"'

    def __repr__(self) -> str:
        return f'Book(id_={self._id}, name={self.name!r}, pages={self.pages})'


if __name__ == '__main__':
    # инициализируем список книг
    list_books = [
        Book(_id=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    for book in list_books:
        print(book)  # проверяем метод __str__

    print(list_books)  # проверяем метод __repr__
    # answer
