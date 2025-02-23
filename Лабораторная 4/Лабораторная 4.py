class Vehicle:
    """
    Базовый класс для всех транспортных средств.
    """

    def __init__(self, brand: str, model: str, year: int) -> None:
        """
        Инициализация атрибутов транспортного средства.

        :param brand: Марка транспортного средства.
        :param model: Модель транспортного средства.
        :param year: Год выпуска транспортного средства.
        """
        self.__brand = brand  # Инкапсуляция, чтобы защитить марку от изменения извне
        self.__model = model  # Инкапсуляция, чтобы защитить модель от изменения извне
        self.year = year

    def __str__(self) -> str:
        """Возвращает строковое представление транспортного средства."""
        return f"{self.year} {self.__brand} {self.__model}"

    def __repr__(self) -> str:
        """Возвращает формальное строковое представление транспортного средства."""
        return f"Vehicle(brand='{self.__brand}', model='{self.__model}', year={self.year})"

    def start_engine(self) -> str:
        """
        Запускает двигатель транспортного средства.

        :return: Сообщение о запуске двигателя.
        """
        return f"The engine of the {self.__brand} {self.__model} is now running."


class Car(Vehicle):
    """
    Класс для легковых автомобилей, наследует от Vehicle.
    """

    def __init__(self, brand: str, model: str, year: int, doors: int) -> None:
        """
        Инициализация атрибутов легкового автомобиля.

        :param brand: Марка легкового автомобиля.
        :param model: Модель легкового автомобиля.
        :param year: Год выпуска легкового автомобиля.
        :param doors: Количество дверей в автомобиле.
        """
        super().__init__(brand, model, year)  # Вызов конструктора базового класса
        self.doors = doors

    def __str__(self) -> str:
        """Возвращает строковое представление легкового автомобиля."""
        return f"{super().__str__()} with {self.doors} doors"

    def honk(self) -> str:
        """
        Подавать сигнал автомобиля.

        :return: Сообщение о сигнале.
        """
        return f"{self.__brand} {self.__model} says honk!"


class Truck(Vehicle):
    """
    Класс для грузовых автомобилей, наследует от Vehicle.
    """

    def __init__(self, brand: str, model: str, year: int, capacity: float) -> None:
        """
        Инициализация атрибутов грузового автомобиля.

        :param brand: Марка грузового автомобиля.
        :param model: Модель грузового автомобиля.
        :param year: Год выпуска грузового автомобиля.
        :param capacity: Грузоподъемность в тоннах.
        """
        super().__init__(brand, model, year)  # Вызов конструктора базового класса
        self.capacity = capacity

    def __str__(self) -> str:
        """Возвращает строковое представление грузового автомобиля."""
        return f"{super().__str__()} with a capacity of {self.capacity} tons"

    def load(self, weight: float) -> str:
        """
        Загружает груз в грузовой автомобиль.

        :param weight: Вес груза в тоннах.
        :return: Сообщение о загрузке.

        Если вес груза превышает грузоподъемность, метод возвращает предупреждение.
        """
        if weight > self.capacity:
            return f"Cannot load {weight} tons. Exceeds capacity of {self.capacity} tons."
        return f"Loaded {weight} tons into the truck."


# Примеры использования классов
if __name__ == "__main__":
    my_car = Car("Toyota", "Corolla", 2020, 4)
    print(my_car)  # Выводит информацию о легковом автомобиле
    print(my_car.start_engine())  # Запуск двигателя
    print(my_car.honk())  # Сигнал автомобиля

    my_truck = Truck("Volvo", "FH", 2018, 20)
    print(my_truck)  # Выводит информацию о грузовом автомобиле
    print(my_truck.start_engine())  # Запуск двигателя
    print(my_truck.load(15))  # Загрузка груза
    print(my_truck.load(25))  # Попытка загрузки превышающего грузоподъемность

