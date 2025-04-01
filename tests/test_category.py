import pytest
from src.category import Category


@pytest.fixture
def categories():
    """Данные для теста класса Category для проверки корректности инициализации"""
    return Category(
        "Телевизоры",
        "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        [{"name": '55" QLED 4K', "description": "Фоновая подсветка", "price": 123000.0, "quantity": 7}],
    )


def test_category_init(categories):
    """Тест проверяющий корректность инициализации в классе Category"""
    assert categories.name == "Телевизоры"
    assert (categories.description == "Современный телевизор, который позволяет наслаждаться просмотром, "
                                      "станет вашим другом и помощником")
    assert categories.products == [
        {"name": '55" QLED 4K', "description": "Фоновая подсветка", "price": 123000.0, "quantity": 7}
    ]
    assert Category.category_count == 1
    assert Category.product_count == 1
