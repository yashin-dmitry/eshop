class Product:
    """
    Класс, представляющий продукт.

    аргументы:
        name (str): Название продукта.
        description (str): Описание продукта.
        price (float): Цена продукта.
        quantity (int): Количество продукта в наличии.

    атрибуты:
        name (str): Название продукта.
        description (str): Описание продукта.
        price (float): Цена продукта.
        quantity (int): Количество продукта в наличии.
    """

    def __init__(self, name: str, description: str, price: float,
                 quantity: int):
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

        self.name = name
        self.description = description
        self._price = price
        self.quantity = quantity

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

    @classmethod
    def new_product(cls, name, description, price, quantity):
        return cls(name, description, price, quantity)

    @property
    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if not isinstance(other, Product):
            raise TypeError("сложение возможно только с другим продуктом")
        return self.price * self.quantity + other.price * other.quantity
