import pytest
from src.product import Product


@pytest.fixture
def product1():
    """Данные для теста класса Product"""
    return Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


def test_product_init(product1):
    """Тест проверяющий корректность инициализации в классе Product"""
    assert product1.name == "Samsung Galaxy C23 Ultra"
    assert product1.description == "256GB, Серый цвет, 200MP камера"
    assert product1.price == 180000.0
    assert product1.quantity == 5
