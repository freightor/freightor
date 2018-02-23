from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shop.models import Store, Merchant, Product, Category, Album, Picture, Order, OrderItem
from shop.forms import ProductForm, CartItemAddForm
from shopping import Cart

# Create your views here.


def product_list(request):
    store = request.user.merchant.store
    queryset = Product.objects.filter(store=store)
    return render(request, "shop/product_list.html", {"products": queryset})


def order_list(request):
    store = request.user.merchant.store
    queryset = OrderItem.objects.filter(store=store)
    return render(request, "shops/order_list.html", {"orders": orders})


def new_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            album = Album()
            for file in request.FILES.getlist("pictures"):
                Picture.objects.create(attachment=file, album=album)
            album.save()
            product.created_by = request.user
            product.save()
            return redirect(request, "shop:product_detail", pk=product.pk)
    else:
        form = ProductForm()
    return render(request, "shop/new_product.html", {"form": form})


def edit_product(request, pk):
    if request.method == "POST":
        store = request.user.merchant.store
        obj = get_object_or_404(Product.objects.filter(store=store), pk=pk)
        form = ProductForm(request.POST, instance=obj)
        if form.is_valid():
            product = form.save(commit=False)
            product.edited_by = request.user
            product.save()
            return redirect(request, "shop:product_detail", pk=product.pk)
    else:
        form = ProductForm()
    return render(request, "shop/new_product.html", {"form": form})


def product_detail(request, pk):
    product = get_object_or_404(Product.objects.filter(active=True), pk=pk)
    form = CartItemAddForm()
    return render(request, "shop/product_detail.html", {"product": product, "form": form})


def shop_home(request):
    queryset = Product.objects.filter(active=True)
    return render(request, "companies/shop_home.html", {"products": queryset})


@require_POST
def add_to_cart(request, pk):
    cart = Cart(request)
    product = get_object_or_404(Product, pk=pk)
    form = CartItemAddForm(request.POST)
    if form.is_valid():
        clean_d = form.cleaned_data
        cart.add_item(
            product=product,
            quantity=clean_d["quantity"],
            update_quantity=clean_d["update"])
        return redirect("shop:cart_detail")


def remove_from_cart(request, pk):
    cart = Cart(request)
    product = get_object_or_404(Product, pk=pk)
    cart.remove_item(product)
    return redirect("shop:cart_detail")


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item["item_update_form"] = CartItemAddForm(
            initial={"quantity": item["quantity"], "update": True})
    return render(request, "shop/cart_detail.html", {"cart": cart})


@require_POST
def cart_checkout(request):
    cart = Cart(request)
    if len(cart) > 0:
        order = Order(employee=request.user)
        cost_count = 0
        for item in cart:
            OrderItem.objects.create(
                order=order,
                product=item["product"],
                quantity=item["quantity"],
                unit_price=item["price"],
                price=item["total_price"],
                store=item["product"].store)
            cost_count += item["total_price"]
        order.total_amount = cost_count
        order.save()
        cart.clear_items()
        return render(request, "shop/order_sent.html", {"order": order})
    return redirect("shop:shop_home")
