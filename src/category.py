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

    def __init__(self, name: str, description: str, products: list[Product]):
        self.name = name
        self.description = description
        self.__products = products

        Category.total_count_category += 1
        Category.total_count_products += len(products)

    def add_product(self, new_product):
        self.__products.append(new_product)