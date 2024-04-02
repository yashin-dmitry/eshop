from abc import ABC, abstractmethod


class AbstractProduct(ABC):
    @abstractmethod
    def __init__(self, name, description, price, quantity):
        self.quantity = quantity
        self.price = price
        self.description = description
        self.name = name

    @property
    @abstractmethod
    def name(self):
        pass

    @name.setter
    @abstractmethod
    def name(self, value):
        pass

    @property
    @abstractmethod
    def description(self):
        pass

    @description.setter
    @abstractmethod
    def description(self, value):
        pass

    @property
    @abstractmethod
    def price(self):
        pass

    @price.setter
    @abstractmethod
    def price(self, value):
        pass

    @price.deleter
    @abstractmethod
    def price(self):
        pass

    @property
    @abstractmethod
    def quantity(self):
        pass

    @quantity.setter
    @abstractmethod
    def quantity(self, value):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __add__(self, other):
        pass


class PrintInfoMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print(f"{type(self).__name__}{repr(self)}")


class Product(PrintInfoMixin, AbstractProduct):
    def __init__(self, name: str, description: str, price: float, quantity: int,
                 *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not isinstance(name, str):
            raise TypeError("имя должно быть строкой")
        if not isinstance(description, str):
            raise TypeError("описание должно быть строкой")
        if not isinstance(price, (int, float)):
            raise TypeError("цена должна быть числом с плавающей точкой"
                            " или целым числом")
        if not isinstance(quantity, int):
            raise TypeError("количество должно быть целым числом")
        if price < 0:
            raise ValueError("цена не может быть отрицательной")
        if quantity < 0:
            raise ValueError("количество не может быть отрицательным")

        self._name = name
        self._description = description
        self._price = price
        self._quantity = quantity

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("имя должно быть строкой")
        self._name = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        if not isinstance(value, str):
            raise TypeError("описание должно быть строкой")
        self._description = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("цена должна быть числом с плавающей точкой"
                            " или целым числом")
        if value < 0:
            raise ValueError("цена не может быть отрицательной")
        self._price = value

    @price.deleter
    def price(self):
        del self._price

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        if not isinstance(value, int):
            raise TypeError("количество должно быть целым числом")
        if value < 0:
            raise ValueError("количество не может быть отрицательным")
        self._quantity = value

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if not isinstance(other, self.__class__):
            raise TypeError(
                f"Невозможно сложить объекты разных классов: "
                f"{type(self).__name__} и {type(other).__name__}")
        return self.price * self.quantity + other.price * other.quantity

    @classmethod
    def new_product(cls, name, description, price, quantity):
        return cls(name, description, price, quantity)


class Smartphone(Product):
    """
    Класс, представляющий смартфон.

    аргументы:
        name (str): Название смартфона.
        description (str): Описание смартфона.
        price (float): Цена смартфона.
        quantity (int): Количество смартфонов в наличии.
        performance (str): Производительность смартфона.
        model (str): Модель смартфона.
        memory_size (int): Объем встроенной памяти смартфона.
        color (str): Цвет смартфона.

    атрибуты:
        name (str): Название смартфона.
        description (str): Описание смартфона.
        price (float): Цена смартфона.
        quantity (int): Количество смартфонов в наличии.
        performance (str): Производительность смартфона.
        model (str): Модель смартфона.
        memory_size (int): Объем встроенной памяти смартфона.
        color (str): Цвет смартфона.
    """

    def __init__(self, name: str, description: str, price: float,
                 quantity: int, performance: str, model: str,
                 memory_size: int, color: str):
        super().__init__(name, description, price, quantity)
        self.performance = performance
        self.model = model
        self.memory_size = memory_size
        self.color = color

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт. " \
               f"Производительность: {self.performance}. " \
               f"Модель: {self.model}. " \
               f"Объем встроенной памяти: {self.memory_size} ГБ. " \
               f"Цвет: {self.color}."


class Grass(Product):
    """
    Класс, представляющий траву газонную.

    аргументы:
        name (str): Название травы.
        description (str): Описание травы.
        price (float): Цена травы.
        quantity (int): Количество травы в наличии.
        country (str): Страна-производитель травы.
        germination_time (str): Срок прорастания травы.
        color (str): Цвет травы.

    атрибуты:
        name (str): Название травы.
        description (str): Описание травы.
        price (float): Цена травы.
        quantity (int): Количество травы в наличии.
        country (str): Страна-производитель травы.
        germination_time (str): Срок прорастания травы.
        color (str): Цвет травы.
    """

    def __init__(self, name: str, description: str, price: float,
                 quantity: int, country: str, germination_time: str,
                 color: str):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_time = germination_time
        self.color = color

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт. " \
               f"Страна-производитель: {self.country}. " \
               f"Срок прорастания: {self.germination_time}. " \
               f"Цвет: {self.color}."
