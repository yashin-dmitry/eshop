import pytest
from src.category import Category
from src.products import Product

def test_category_init():
    category = Category("Test Category", "Test Description")
    assert category.name == "Test Category"
    assert category.description == "Test Description"
    assert category.total_count_category == 1
    assert category.total_count_products == 0

def test_category_add_product():
    category = Category("Test Category", "Test Description")
    product = Product("Test Product", "Test Product Description", 100, 5)
    category.add_product(product)
    assert category.total_count_products == 1

def test_category_products_property():
    category = Category("Test Category", "Test Description")
    product1 = Product("Test Product 1", "Test Product 1 Description", 100, 5)
    product2 = Product("Test Product 2", "Test Product 2 Description", 200, 10)
    category.add_product(product1)
    category.add_product(product2)
    assert category.products == "Test Product 1, 100 руб. Остаток: 5 шт.\nTest Product 2, 200 руб. Остаток: 10 шт."


def test_category_total_count_category():
    Category.total_count_category = 0
    Category("Test Category1", "Test Description1")
    Category("Test Category2", "Test Description2")
    assert Category.total_count_category == 2

def test_category_total_count_products():
    Category.total_count_category = 0
    Category.total_count_products = 0
    category = Category("Test Category", "Test Description")
    product1 = Product("Test Product 1", "Test Product 1 Description", 100, 5)
    product2 = Product("Test Product 2", "Test Product 2 Description", 200, 10)
    category.add_product(product1)
    category.add_product(product2)
    assert Category.total_count_products == 2
