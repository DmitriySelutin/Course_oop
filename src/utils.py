from abc import ABC, abstractmethod
from typing import Any


class BaseProduct(ABC):
    """базовый класс"""

    @abstractmethod
    def new_product(self, *args, **kwargs):
        """абстрактный метод"""
        pass


class Mixin:
    """класс Миксин"""

    def __init__(self, *args, **kwargs):
        """инициализация класса миксин"""
        super().__init__(*args, **kwargs)
        print(repr(self))

    def __repr__(self):
        """вывод для разработчика"""
        return f"Создан объект класса {self.__class__.__name__}: {self}"


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
        """метод для получения продуктов"""
        return self.__products

    @property
    def product_list_enter(self):
        """Метод вывода информации о продукте."""
        list_product = []
        for product in self.__products:
            result = f"{self.name}, {product.price} руб. Остаток: {product.quantity} шт."
            list_product.append(result)
        return list_product

    def __len__(self):
        """Магический метод, который вызывается при применении функции len"""
        return len(self.__products)

    def __str__(self):
        """Магический метод для строкового отображения объекта"""
        return f"{self.name}, количество продуктов: {len(self.__products)} шт."

    def calculate_average_price(self):
        """Вычисляет среднюю цену для всех товаров в категории."""
        try:
            total_price = sum(product.price for product in self.__products)
            average_price = total_price / len(self.__products)
            return average_price
        except ZeroDivisionError:
            return 0.0


class Product(BaseProduct, Mixin):
    """Класс продуктов"""

    name: str
    description: str
    _price: float
    quantity: int

    def __init__(self, name, description, price, quantity, *args, **kwargs):
        """метод для инициализации экземпляра класса"""
        self.name = name
        self.description = description
        self._price = price
        self.quantity = quantity
        super().__init__(*args, **kwargs)

    @classmethod
    def create_and_add_to_products(
        cls,
        products_list: list,
        name: str,
        description: str,
        price: float,
        quantity: int,
    ) -> Any:
        """Метод для создания товара и добавления его в список товаров с проверкой наличия дубликата."""
        for product in products_list:
            if product.name == name:
                if product._price < price:
                    product._price = price
                product.quantity += quantity
                return product

        # Проверяем, что объект является экземпляром класса Product или его наследником
        if (
            not isinstance(name, str)
            or not isinstance(description, str)
            or not isinstance(price, float)
            or not isinstance(quantity, int)
        ):
            raise TypeError("Неверный тип данных для создания продукта")

        if quantity == 0:
            raise ValueError("Tовар с нулевым количеством не может быть добавлен.")

        new_product = cls(name, description, price, quantity)
        products_list.append(new_product)
        return products_list

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

    def __str__(self):
        """Магический метод для строкового отображения объекта"""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """Магический метод, который вызывается при сложении двух объектов"""
        if type(self) is type(other):
            raise TypeError("Можно складывать только одинаковые типы продуктов")
        return self.price * self.quantity + other.price * other.quantity

    def new_product(self, *args, **kwargs):
        """реализация метода new_product"""
        pass


class Smartphone(Product, Mixin):
    """Класс смартфон"""

    performance: int
    model: str
    memory: int
    color: str

    def __init__(self, name, description, price, quantity, performance, model, memory, color):
        """метод инициализации объекта"""
        self.performance = performance
        self.model = model
        self.memory = memory
        self.color = color
        super().__init__(name, description, price, quantity)

    def new_product(self, *args, **kwargs):
        """реализация метода new_product"""
        pass


class LawnGrass(Product, Mixin):
    """класс трава газонная"""

    country: str
    term: int
    color: str

    def __init__(self, name, description, price, quantity, country, term, color):
        """метод инициализации объекта"""
        self.country = country
        self.term = term
        self.color = color
        super().__init__(name, description, price, quantity)

    def new_product(self, *args, **kwargs):
        """реализация метода new_product"""
        pass
