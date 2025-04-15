import pytest
from src.lawngrass import LawnGrass


@pytest.fixture
def lawngrass():
    """Данные для теста lawngrass"""
    return LawnGrass.new_product({
        "name": "Lawngrass",
        "description": "Lawngrass small size",
        "price": 2000.0,
        "quantity": 7,
        "country": "Russia",
        "germination_period": "1 month",
        "color": "Зелёный"
    })


def test_lawngrass_init(lawngrass):
    assert lawngrass.name == "Lawngrass"
    assert lawngrass.description == "Lawngrass small size"
    assert lawngrass.price == 2000.0
    assert lawngrass.quantity == 7
    assert lawngrass.country == "Russia"
    assert lawngrass.germination_period == "1 month"
    assert lawngrass.color == "Зелёный"
