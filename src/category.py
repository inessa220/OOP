class Category:
    """Класс предоставляющий иинформацию о категории товара, количестве товаров в категории и количестве категорий"""
    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        """Инициализация объекта"""
        self.name = name
        self.description = description
        self.products = products if products else []
        Category.category_count += 1
        Category.product_count = len(products) if products else 0
