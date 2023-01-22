import doctest


class Paper:
    def __init__(self, size: float, colour: str):
        """
        Создание и подготовка к работе объекта "Бумага"
        :param size: Формат бумаги
        :param colour: Цвет бумаги
        Примеры:
        >>> pebble = Paper(4.0, "table")  # инициализация экземпляра класса
        """
        if not isinstance(size, float):
            raise TypeError("Размер бумаги может быть только числом")
        self.size = size
        if not isinstance(colour, str):
            raise TypeError("Цвет бумаги может быть только строкой")
        self.colour = colour

    def lay(self) -> bool:
        """
        Положить бумагу
        Примеры:
        >>> pebble = Paper(4.0, "table")
        >>> pebble.lay()
        """
        ...

    def take(self) -> bool:
        """
        Поднять бумагу
        Примеры:
        >>> pebble = Paper(4.0, "table")
        >>> pebble.take()
        """
        ...


class Samurai:
    def __init__(self, name: str, membership: str):
        """
        Создание и подготовка к работе объекта "Самурай"
        :param name: имя самурая
        :param membership: принадлежность самурая
        Примеры:
        >>> pip = Samurai("V", "Arasaka")  # инициализация экземпляра класса
        """
        if not isinstance(name, str):
            raise TypeError("Имя самурая может быть только строкой")
        self.name = name

        if not isinstance(membership, str):
            raise TypeError("Принадлежность самурая может быть только строкой")
        self.membership = membership

    def wakeup(self) -> str:
        """
        Разбудить самурая
        :return: "self.name" спит. Повторите эту команду через час
        Примеры:
        >>> pip = Samurai("V", "Arasaka")
        >>> pip.wakeup()
        """
        ...

    def burn(self) -> str:
        """
        Время самураю жечь город
        :return: "self.name" готов
        Примеры:
        >>> pip = Samurai("V", "Arasaka")
        >>> pip.burn()
        """
        ...


class Box:
    def __init__(self, capacity: int, occupied: int):
        """
        Создание и подготовка к работе объекта "Коробка"
        :param capacity: Вместимость коробки
        :param occupied: Занятость коробки
        Примеры:
        >>> crayonbox = Box(12, 0)  # инициализация экземпляра класса
        """
        if not isinstance(capacity, int):
            raise TypeError("Вместимость коробки должна быть целочисленной")
        if capacity <= 0:
            raise ValueError("Вместимость коробки не может быть отрицательным")
        self.capacity = capacity

        if not isinstance(occupied, int):
            raise TypeError("Занятость короюки должна быть численной")
        if occupied < 0:
            raise ValueError("Занятость коробки не может быть отрицательной")
        self.occupied = occupied

    def add_crayon(self, crayon: int) -> None:
        """
        Добавление карандашей в коробку.
        :param crayon: Кол-во добавляемых карандашей
        :raise ValueError: Если количество добавляемых карандашей больше вместимости коробки
        Примеры:
        >>> crayonbox = Box(12, 0)
        >>> crayonbox.add_crayon(3)
        """
        if not isinstance(crayon, int):
            raise TypeError("Кол-во добавляемых карандашей должно быть целым")
        if crayon < 0:
            raise ValueError("Кол-во добавляемых карандашей не может быть отрицательным")
        ...

    def take(self, volume: int) -> int:
        """
        Достать карандаш из коробки
        :param volume: Кол-во карандашей
        :raise ValueError: Если кол-во карандашей превышает вместимость коробки, то возвращается ошибка
        :return: Оставшийся кол-во карандашей в чашке
        Примеры:
        >>> crayonbox = Box(12, 4)
        >>> crayonbox.take(2)
        """
        ...


if __name__ == "__main__":
    doctest.testmod()  
    # тестирование
