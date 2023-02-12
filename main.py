import datetime


class Automobile:
    """Базовый класс "Автомобили"."""
    def __init__(self, manufacturer: str, model: str, year: int, max_speed: int, capacity: int,
                 mileage: int):
        """
        :param manufacturer: Производитель
        :param model: Модель
        :param year: Год производства
        :param max_speed: Максимально возможная скорость
        :param capacity: Вместимость
        :param mileage: Пробег
        """
        self._manufacturer = manufacturer
        self._model = model
        if not isinstance(year, int):
            raise TypeError('Год производства должен быть типа int')
        if year <= 0:
            raise ValueError('Год производства должен быть положительным числом')
        self.year = year
        if not isinstance(max_speed, int):
            raise TypeError('Максимально возможная скорость должна быть типа int')
        if max_speed <= 0:
            raise ValueError('Максимально возможная скорость должна быть положительным числом')
        self.max_speed = max_speed
        if not isinstance(capacity, int):
            raise TypeError('Вместимость должна быть типа int')
        if capacity <= 0:
            raise ValueError('Вместимость должна быть положителным числом')
        self.capacity = capacity
        if not isinstance(mileage, int):
            raise TypeError('Пробег должен быть типа float')
        if mileage <= 0:
            raise ValueError('Пробег должен быть положительным числом')
        self.mileage = mileage

    # информация о изготовителе и модели неизменяема
    @property
    def manufacturer(self) -> str:
        return self._manufacturer

    @property
    def model(self) -> str:
        return self._model

    def __str__(self) -> str:
        return f"Производитель {self.manufacturer}. Модель {self.model}. Год производства  {self.year}. " \
               f"Максимально возможная скорость {self.max_speed} км/ч, вместимость {self.capacity}, " \
               f"пробег {self.mileage} км."

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(manufacturer={self.manufacturer!r}, model={self.model!r}, " \
               f"mileage={self.mileage}" \


    def usage_time(self) -> int:
        """Метод определяет период владения автомобилем."""
        return datetime.date.today().year - self.year


class Motorcar(Automobile):
    """Дочерний класс "Автомобиль с ДВС"."""

    def __init__(self, manufacturer: str, model: str, year: int, max_speed: int, capacity: int,
                 mileage: int, fuel_tank_capacity: int):
        """
        :param manufacturer: Производитель
        :param model: Модель
        :param year: Год производства
        :param max_speed: Максимально возможная скорость
        :param capacity: Вместимость
        :param mileage: Пробегм
        :param fuel_tank_capacity: Вместимость топливного бака [л]
        """
        super().__init__(manufacturer, model, year, max_speed, capacity, mileage)
        if not isinstance(fuel_tank_capacity, int):
            raise TypeError('Вместимость топливного бака должна быть типа int')
        if fuel_tank_capacity <= 0:
            raise ValueError('Вместимость топливного бака должна быть положительным числом')
        self.fuel_tank_capacity = fuel_tank_capacity

    def __str__(self) -> str:
        return f"Производитель {self.manufacturer}. Модель {self.model}. Год производства  {self.year}. " \
               f"Максимально возможная скорость {self.max_speed} км/ч, вместимость {self.capacity}, " \
               f"расхол {self.fuel_tank_capacity} л."

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(manufacturer={self.manufacturer!r}, model={self.model!r}, " \
               f"year={self.year}, max_speed={self.max_speed}, capacity={self.capacity}," \
               f"fuel_tank_capacity={self.fuel_tank_capacity})"

    def fuel_consumption(self) -> float:
        """Метод определяет расход топлива на 100 километров."""
        return self.fuel_tank_capacity / (self.mileage * 100)


class Electriccar(Automobile):
    """Дочерний класс "Электромобиль"."""
    def __init__(self, manufacturer: str, model: str, year: int, max_speed: int, capacity: int,
                 mileage: int, power_capacity: int):
        """
        :param manufacturer: Производитель
        :param model: Модель
        :param year: Год производства
        :param max_speed: Максимально возможная скорость
        :param capacity: Вместимость
        :param mileage: Пробег
        :param power_capacity: Емкость батареи [кВт*ч]
        """
        super().__init__(manufacturer, model, year, max_speed, capacity, mileage)
        if not isinstance(power_capacity, int):
            raise TypeError('Емкость батареи должна быть типа int')
        if power_capacity <= 0:
            raise ValueError('Емкость батареи должна быть положительным числом')
        self.power_capacity = power_capacity

    def __str__(self) -> str:
        return f"Производитель {self.manufacturer}. Модель {self.model}. Год производства  {self.year}. " \
               f"Максимально возможная скорость {self.max_speed} км/ч, вместимость {self.capacity}, " \
               f"расхол {self.power_capacity} кВт*ч."

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(manufacturer={self.manufacturer!r}, model={self.model!r}, " \
               f"year={self.year}, max_speed={self.max_speed}, capacity={self.capacity}, " \
               f"power_capacity={self.power_capacity})"

    def fuel_consumption(self) -> float:
        """Метод определяет расход электроэнергии за рейс."""
        return self.power_capacity * self.mileage / 100


if __name__ == "__main__":
    transport = Automobile('Toyota', 'RAV4»', 2016, 180, 8, 155396)
    print(transport)
    transport.usage_time()
    car = Motorcar('Kia', 'Optima', 2018, 202, 5, 70, 11)
    print(car)
    car.fuel_consumption()
    electric_vehicle = Electriccar('Tesla', 'Model 3', 2019, 233, 5, 50, 15)
    print(electric_vehicle)
    electric_vehicle.fuel_consumption()

    pass
