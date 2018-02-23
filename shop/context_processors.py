from shop.shopping import Cart


def cart(request):
    return {"cart": Cart(request)}
