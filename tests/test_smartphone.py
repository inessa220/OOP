import pytest
from src.smartphone import Smartphone


@pytest.fixture
def smartphone():
    """Данные для теста Smartphone"""
    return Smartphone.new_product({
        "name": "Samsung Galaxy C23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5,
        "efficiency": "3.4 Ггц",
        "model": "Galaxy C23 Ultra",
        "memory": "256Gb",
        "color": "Серый"
    })


def test_smartphone_init(smartphone):
    assert smartphone.name == "Samsung Galaxy C23 Ultra"
    assert smartphone.description == "256GB, Серый цвет, 200MP камера"
    assert smartphone.price == 180000.0
    assert smartphone.quantity == 5
    assert smartphone.efficiency == "3.4 Ггц"
    assert smartphone.model == "Galaxy C23 Ultra"
    assert smartphone.memory == "256Gb"
    assert smartphone.color == "Серый"
