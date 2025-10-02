import unittest
from shoppingCart import ShoppingCart, Item

class TestShoppingCart(unittest.TestCase):
    def setUp(self):
        self.cart = ShoppingCart()
    def test_addItem(self):
        item = Item("Book", 12.99)
        self.cart.addItem(item)
        self.assertIn(item, self.cart.items)
    def test_removeItem(self):
        item = Item("Book", 12.99)
        self.cart.addItem(item)
        self.cart.removeItem(item)
        self.assertNotIn(item, self.cart.items)
    def test_totalPrice(self):
        item1 = Item("Book", 12.99)
        item2 = Item("Pen", 1.99)
        self.cart.addItem(item1)
        self.cart.addItem(item2)
        self.assertEqual(self.cart.totalPrice(), 14.98)


if __name__ == "__main__":
    unittest.main()