import doctest

class Car:
    def __init__(self, make: str, model: str, year: int, mileage: float = 0.0):
        """
        Создание и подготовка к работе объекта "Автомобиль"

        :param make: Производитель автомобиля
        :param model: Модель автомобиля
        :param year: Год выпуска
        :param mileage: Пробег автомобиля в километрах

        :raise TypeError: Если типы аргументов не соответствуют ожидаемым
        :raise ValueError: Если значения аргументов не допустимы (например, отрицательные значения)

        Примеры:
        >>> car = Car("Toyota", "Corolla", 2020)
        """
        if not isinstance(make, str):
            raise TypeError("Производитель автомобиля должен быть строкой")
        if not isinstance(model, str):
            raise TypeError("Модель автомобиля должна быть строкой")
        if not isinstance(year, int):
            raise TypeError("Год выпуска должен быть целым числом")
        if not isinstance(mileage, (int, float)):
            raise TypeError("Пробег должен быть числом")
        if year < 1886:  # Первый автомобиль был создан в 1886 году
            raise ValueError("Год выпуска не может быть ранее 1886 года")
        if mileage < 0:
            raise ValueError("Пробег не может быть отрицательным числом")

        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage

    def drive(self, kilometers: float) -> None:
        """
        Увеличивает пробег автомобиля.

        :param kilometers: Количество километров для добавления к пробегу

        :raise TypeError: Если kilometers не число
        :raise ValueError: Если kilometers отрицательно

        Примеры:
        >>> car = Car("Honda", "Civic", 2018)
        >>> car.drive(150.5)
        """
        if not isinstance(kilometers, (int, float)):
            raise TypeError("Количество километров должно быть числом")
        if kilometers < 0:
            raise ValueError("Количество километров не может быть отрицательным")
        self.mileage += kilometers
        ...

    def repaint(self, color: str) -> None:
        """
        Перекрашивает автомобиль в указанный цвет.

        :param color: Новый цвет автомобиля

        :raise TypeError: Если color не строка
        :raise ValueError: Если color пустая строка

        Примеры:
        >>> car = Car("Ford", "Mustang", 2021)
        >>> car.repaint("Красный")
        """
        if not isinstance(color, str):
            raise TypeError("Цвет должен быть строкой")
        if not color.strip():
            raise ValueError("Цвет не может быть пустой строкой")
        self.color = color
        ...


class BankAccount:
    def __init__(self, account_number: str, owner: str, balance: float = 0.0):
        """
        Создание и подготовка к работе объекта "Банковский счет"

        :param account_number: Номер банковского счета
        :param owner: Владелец счета
        :param balance: Текущий баланс счета

        :raise TypeError: Если типы аргументов не соответствуют ожидаемым
        :raise ValueError: Если значения аргументов не допустимы (например, отрицательные значения)

        Примеры:
        >>> account = BankAccount("1234567890", "Иван Иванов")
        """
        if not isinstance(account_number, str):
            raise TypeError("Номер счета должен быть строкой")
        if not isinstance(owner, str):
            raise TypeError("Владелец счета должен быть строкой")
        if not isinstance(balance, (int, float)):
            raise TypeError("Баланс должен быть числом")
        if balance < 0:
            raise ValueError("Баланс не может быть отрицательным числом")

        self.account_number = account_number
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: float) -> None:
        """
        Вносит указанную сумму на счет.

        :param amount: Сумма для внесения

        :raise TypeError: Если amount не число
        :raise ValueError: Если amount не положительно

        Примеры:
        >>> account = BankAccount("0987654321", "Мария Петрова")
        >>> account.deposit(500.0)
        """
        if not isinstance(amount, (int, float)):
            raise TypeError("Сумма должна быть числом")
        if amount <= 0:
            raise ValueError("Сумма должна быть положительным числом")
        self.balance += amount
        ...

    def withdraw(self, amount: float) -> None:
        """
        Снимает указанную сумму со счета.

        :param amount: Сумма для снятия

        :raise TypeError: Если amount не число
        :raise ValueError: Если amount не положительно или превышает текущий баланс

        Примеры:
        >>> account = BankAccount("1122334455", "Алексей Смирнов", 1000.0)
        >>> account.withdraw(200.0)
        """
        if not isinstance(amount, (int, float)):
            raise TypeError("Сумма должна быть числом")
        if amount <= 0:
            raise ValueError("Сумма должна быть положительным числом")
        if amount > self.balance:
            raise ValueError("Недостаточно средств на счете")
        self.balance -= amount
        ...


class MusicPlayer:
    def __init__(self, brand: str, model: str, battery_life: float):
        """
        Создание и подготовка к работе объекта "Музыкальный плеер"

        :param brand: Бренд плеера
        :param model: Модель плеера
        :param battery_life: Время работы от батареи в часах

        :raise TypeError: Если типы аргументов не соответствуют ожидаемым
        :raise ValueError: Если значения аргументов не допустимы (например, отрицательные значения)

        Примеры:
        >>> player = MusicPlayer("Sony", "Walkman", 15.0)
        """
        if not isinstance(brand, str):
            raise TypeError("Бренд плеера должен быть строкой")
        if not isinstance(model, str):
            raise TypeError("Модель плеера должна быть строкой")
        if not isinstance(battery_life, (int, float)):
            raise TypeError("Время работы от батареи должно быть числом")
        if battery_life <= 0:
            raise ValueError("Время работы от батареи должно быть положительным числом")

        self.brand = brand
        self.model = model
        self.battery_life = battery_life
        self.current_battery = battery_life

    def play_music(self, duration: float) -> None:
        """
        Воспроизводит музыку в течение указанного времени.

        :param duration: Время воспроизведения в часах

        :raise TypeError: Если duration не число
        :raise ValueError: Если duration не положительно или превышает оставшееся время работы батареи

        Примеры:
        >>> player = MusicPlayer("Apple", "iPod", 10.0)
        >>> player.play_music(2.5)
        """
        if not isinstance(duration, (int, float)):
            raise TypeError("Время воспроизведения должно быть числом")
        if duration <= 0:
            raise ValueError("Время воспроизведения должно быть положительным числом")
        if duration > self.current_battery:
            raise ValueError("Недостаточно заряда батареи для воспроизведения музыки")
        self.current_battery -= duration
        ...

    def recharge(self, hours: float) -> None:
        """
        Заряжает плеер на указанное количество часов.

        :param hours: Время зарядки в часах

        :raise TypeError: Если hours не число
        :raise ValueError: Если hours не положительно или превышает максимальное время зарядки

        Примеры:
        >>> player = MusicPlayer("Samsung", "Galaxy Player", 8.0)
        >>> player.recharge(3.0)
        """
        if not isinstance(hours, (int, float)):
            raise TypeError("Время зарядки должно быть числом")
        if hours <= 0:
            raise ValueError("Время зарядки должно быть положительным числом")
        if self.current_battery + hours > self.battery_life:
            raise ValueError("Время зарядки превышает максимальную емкость батареи")
        self.current_battery += hours
        ...


if __name__ == "__main__":
    doctest.testmod()
