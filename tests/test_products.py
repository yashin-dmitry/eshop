import pytest
from src.products import Product

def test_product_init():
    """
    Проверяет, что экземпляр класса Product инициализируется с правильными значениями атрибутов.
    """
    product = Product("Test product", "Test product description", 10.0, 5)
    assert product.name == "Test product"
    assert product.description == "Test product description"
    assert product.price == 10.0
    assert product.quantity == 5

def test_product_name_type():
    """
    Проверяет, что аргумент name имеет тип str.
    """
    with pytest.raises(TypeError):
        Product(123, "Test product description", 10.0, 5)

def test_product_description_type():
    """
    Проверяет, что аргумент description имеет тип str.
    """
    with pytest.raises(TypeError):
        Product("Test product", 123, 10.0, 5)

def test_product_price_type():
    """
    Проверяет, что аргумент price имеет тип float или int.
    """
    with pytest.raises(TypeError):
        Product("Test product", "Test product description", "10.0", 5)

def test_product_quantity_type():
    """
    Проверяет, что аргумент quantity имеет тип int.
    """
    with pytest.raises(TypeError):
        Product("Test product", "Test product description", 10.0, "5")

def test_product_price_value():
    """
    Проверяет, что значение аргумента price неотрицательно.
    """
    with pytest.raises(ValueError):
        Product("Test product", "Test product description", -10.0, 5)

def test_product_quantity_value():
    """
    Проверяет, что значение аргумента quantity неотрицательно.
    """
    with pytest.raises(ValueError):
        Product("Test product", "Test product description", 10.0, -5)
