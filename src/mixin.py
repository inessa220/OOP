class Mixin:
    """Миксин, который выводит в консоль информациюЖ от какого класса и с какими параметрами был создан объект"""
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self):
        print(repr(self))

    def __repr__(self):
        """Выводит в консоль информацию, согласно шаблону"""
        return f"{self.__class__.__name__} ({self.name}, {self.description}, {self.price}, {self.quantity})"
