class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class ShoppingCart:
    def __init__(self):
        self.items = []

    def addItem(self, item):
        self.items.append(item)
    
    def removeItem(self, item):
        if item in self.items:
            self.items.remove(item)
    
    def totalPrice(self):
        return sum(item.price for item in self.items)
