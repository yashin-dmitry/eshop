import pytest
from src.category import Category


def test_category_initialization():
    """
    Проверяет, что категория инициализируется с правильными аргументами и атрибутами.
    """
    products = ["apple", "banana", "orange"]
    category = Category("Fruits", "Fruit category", products)
    assert category.name == "Fruits"
    assert category.description == "Fruit category"
    assert category.products == products
    assert Category.total_count_category == 1
    assert Category.total_count_products == 3

def test_multiple_categories():
    """
    Проверяет, что несколько категорий инициализируются с правильными атрибутами.
    """
    products1 = ["apple", "banana", "orange"]
    products2 = ["potato", "onion", "carrot"]
    category1 = Category("Fruits", "Fruit category", products1)
    category2 = Category("Vegetables", "Vegetable category", products2)
    assert Category.total_count_category == 3
    assert Category.total_count_products == 9

def test_empty_products():

    """
    Проверяет, что категория может быть создана с пустым списком продуктов.
    """
    category = Category("Empty", "Empty category", [])
    assert category.products == []
    assert Category.total_count_category == 4
    assert Category.total_count_products == 9
