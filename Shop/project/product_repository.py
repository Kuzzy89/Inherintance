from typing import List
from project.product import Product


class ProductRepository:
    def __init__(self):
        self.products: List[Product] = []

    def add(self, product):
        self.products.append(product)

    def find(self, name):
        res = [p for p in self.products if p.name == name]
        if res:
            return res[0]

    def remove(self, name):
        product = self.find(name)
        if product:
            self.products.remove(name)

    def __repr__(self):
        if self.products:
            return "\n".join([f"{p.name}: {p.quantity}"for p in self.products])
