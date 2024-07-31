class Category:
    """Класс категорий"""
    name: str
    description: str
    __products: list
    all_category = 0
    all_unic_product = 0

    def __init__(self, name, description, products):
        """метод для инициализации экземпляра класса"""
        self.name = name
        self.description = description
        self.__products = products

        Category.all_category += 1
        Category.all_unic_product += len(self.__products)

    @classmethod
    def add_products(cls, product):
        """метод для добавления продуктов"""
        cls.__products.append(product)

    def get_products(self):
        """метод для получения продкутов"""
        return self.__products

    @property
    def get_products_list(self):
        """геттер для вывода информации о продукте"""
        for product in self.__products:
            return f"{self.name}, {product.price} руб. Остаток: {product.quantity} шт."


class Product:
    """Класс продуктов"""
    name: str
    description: str
    _price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        """метод для инициализации экземпляра класса"""
        self.name = name
        self.description = description
        self._price = price
        self.quantity = quantity

    @classmethod
    def create_and_add_to_products(cls, product_list, name, description, price, quantity):
        """метод для создания товара и добавление его в список товаров с проверкой наличия дубликатов"""
        for product in product_list:
            if product.name == name:
                if product._price < price:
                    product._price = price
                product.quantity += quantity
                return product
        new_product = cls(name, description, price, quantity)
        product_list.append(new_product)
        return product_list

    @property
    def price(self):
        """геттер для атрибута цены"""
        return self._price

    @price.setter
    def price(self, new_price):
        """сеттер для атрибута цены"""
        if new_price <= 0:
            print("Цена введена некорректно")
        else:
            self._price = new_price
            print(self._price)
            print("Цена успешно изменена")
