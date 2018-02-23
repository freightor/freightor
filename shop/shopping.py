class CartItem:
    def __init__(self, item, quantity):
        self.item = item
        self.quantity = quantity

    def increase(self):
        self.quantity += 1

    def decrease(self):
        self.quantity -= 1


class Cart:
    def __init__(self, user, items=[]):
        self.user = user
        self.items = items

    def add_item(self, item, quantity):
        self.items[item] = quantity

    def remove_item(self, item):
        self.items.pop(item)

    def clear_cart(self):
        self.items.clear()
