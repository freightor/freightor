from decimal import Decimal
from django.utils import timezone
from django.conf import settings
from shop.models import Product


class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def add_item(self, product, quantity=1, update_quantity=False):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {
                "quantity": quantity, "price": str(product.new_price)}

        if update_quantity:
            self.cart[product_id]["quantity"] = quantity
        else:
            self.cart[product_id]["quantity"] += 1
        self.save()

    def remove_item(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        product_list = self.cart.keys()
        products = Product.objects.filter(id__in=product_list)
        for product in products:
            self.cart[str(product.id)]["product"] = product

        for item in self.cart.values():
            item["price"] = Decimal(item["price"])
            item["total_price"] = item["price"]*item["quantity"]
            yield item

    def __len__(self):
        return sum(item["quantity"] for item in self.cart.values())
    
    def total_amount(self):
        return sum(item["total_price"] for item in self.cart.values())

    def clear_items(self):
        self.session[settings.CART_SESSION_ID].clear()
        self.session.modified = True
