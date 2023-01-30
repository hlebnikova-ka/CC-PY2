from typing import Optional

from pydantic import BaseModel


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



class Library(BaseModel):
    books: Optional[list] = []

    def get_next_book_id(self):
                if self.books == []:
            return 1
        else:
            return self.books[-1]._id +1

    def get_index_by_book_id(self, book_id: int):
        if not isinstance(book_id, int):
            raise TypeError("Введите целое число в поле id")
        book_index = None
        list_id = []
        for i in range(len(self.books)):
            list_id.append(self.books[i]._id)
        for index, current_id in enumerate(list_id):
            if current_id == book_id:
                book_index = index
        if book_index is None:
            raise ValueError("Книга с данным id отсутствует")
        return book_index


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(_id=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
    # answer
