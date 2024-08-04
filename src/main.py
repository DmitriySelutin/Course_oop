from src.utils import Category, Product

product1 = Product("Яблоко", "зеленое", 100, 5)
product2 = Product("Яблоко", "красное", 125, 10)
product3 = Product("Яблоко", "желтое", 110, 8)

categories = Category("Фрукты", "импортные", [product1, product2, product3])


for product in categories.product_list_enter:
    print(product)
