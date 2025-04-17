from _pytest.capture import CaptureFixture
from src.product import Product


def test_print_mixin(capsys: CaptureFixture[str]) -> None:
    """Тестируем поведение класса-миксин при добавлении товаров разных классов"""
    Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    message = capsys.readouterr()
    assert message.out.strip() == "Product (Iphone 15, 512GB, Gray space, 210000.0, 8)"
