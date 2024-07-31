import pytest
from src.utils import Category, Product


@pytest.fixture
def product1():
    """Создание экземпляра класса Продукт"""
    return Product("топ", "для занятия спортом", 599, 10)


@pytest.fixture
def product2():
    """Создание экземпляра класса Продукт"""
    return Product("топ2", "для занятия спортом2", 599, 10)


@pytest.fixture
def category_object(product1, product2):
    """создание экземпляра класса Категория"""
    return Category("одежда", "для спорта", [product1, product2])


def test_init_category(category_object, product1, product2):
    """
    Тест проверяет корректность инициализации объектов класса Category.
    Также тест считает количество продуктов и категорий.
    """
    assert category_object.name == "одежда"
    assert category_object.description == "для спорта"
    assert category_object.products == [product1, product2]
    assert category_object.all_category == 1
    assert category_object.all_unic_product == 2


def test_init_product(product1):
    """Тест проверяет корректность инициализации объектов класса Product"""
    assert product1.name == "топ"
    assert product1.description == "для занятия спортом"
    assert product1.price == 599
    assert product1.quantity == 10
