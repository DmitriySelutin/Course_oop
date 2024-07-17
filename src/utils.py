class Category:
    """Класс категорий"""
    name: str
    description: str
    products: list
    all_category = 0
    all_unic_product = 0

    def __init__(self, name, description, products):
        """метод для инициализации экземпляра класса"""
        self.name = name
        self.description = description
        self.products = products
        self.all_category += 1
        self.all_unic_product = len(set([product.name for product in self.products]))


class Product:
    """Класс продуктов"""
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        """метод для инициализации экземпляра класса"""
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
