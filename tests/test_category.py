import pytest
from src.category import Category
from src.product import Product


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
    assert Category.category_count == 1
    assert Category.product_count == 1


@pytest.fixture
def data_for_counters_categories():
    """Данные для теста класса Category для проверки вывода"""
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для " "удобства жизни",
        [
            Product.new_product(
                {"name": "Iphone 15", "description": "512GB, Gray space", "price": 210000.0, "quantity": 8}
            ),
            Product.new_product(
                {"name": "Xiaomi Redmi Note 11", "description": "1024GB, Синий", "price": 31000.0, "quantity": 14}
            ),
        ],
    )


def test_category_products(data_for_counters_categories):
    """Проверка корректности вывода строки"""
    assert data_for_counters_categories.products == (
        'Iphone 15, 210000.0 руб. Остаток: 8 шт.\nXiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.\n')


def test_category_str(data_for_counters_categories):
    assert str(data_for_counters_categories) == 'Смартфоны, количество продуктов: 22 шт.'


@pytest.fixture
def first_category() -> Category:
    return Category(
        name="Смартфоны",
        description="Смартфоны, как средство не только коммуникации, но и получения дополнительных функций",
        products=[
            Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5),
            Product("Iphone 15", "512GB, Gray space", 210000.0, 8),
            Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14),
        ],
    )


def test_middle_price(first_category: Category) -> None:
    """Проверка подсчета среднего ценника товаров"""
    category_empty = Category("Пустая категория", "Категория без продуктов", [])
    assert first_category.middle_price() == 111629.63
    assert category_empty.middle_price() == 0
