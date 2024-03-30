from src.products import Product


class Category:
    """
    Класс, представляющий категорию продуктов.

    аргументы:
        name (str): Название категории.
        description (str): Описание категории.

    атрибуты:
        name (str): Название категории.
        description (str): Описание категории.
        products (list): Список продуктов в категории.
    """
    total_count_category = 0
    total_count_products = 0

    def __init__(self, name: str, description: str,
                 products: list[Product] = None):
        self.name = name
        self.description = description
        self.__products = products if products is not None else []

        Category.total_count_category += 1
        Category.total_count_products += len(self.__products)

    def add_product(self, new_product):
        self.__products.append(new_product)
        Category.total_count_products += 1

    @property
    def products(self):
        return '\n'.join([f"{product.name}, {product.price} руб. Остаток: "
                          f"{product.quantity} шт."
                          for product in self.__products])

    def __len__(self):
        return sum(product.quantity for product in self.__products)

    def __str__(self):
        return f"{self.name}, количество продуктов: {len(self)} шт."

    def add_product(self, product):
        if not isinstance(product, Product) and not issubclass(type(product),
                                                               Product):
            raise TypeError(
                "Можно добавлять только продукты или их наследников")
        self.__products.append(product)
        Category.total_count_products += 1

    def __add__(self, other):
        if type(self) != type(other):
            raise TypeError("Можно складывать только объекты одного класса")
        new_category = Category(self.name + " + " + other.name,
                                self.description + " + " + other.description)
        new_category.__products = self.__products + other.__products
        new_category.total_count_products = len(new_category.__products)
        return new_category