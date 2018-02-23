from django.shortcuts import render, redirect, get_object_or_404
from shop.models import Store, Merchant, Product, Category, Album, Picture
from shop.forms import ProductForm
from shopping import Cart, CartItem

# Create your views here.


def product_list(request):
    store = request.user.merchant.store
    queryset = Product.objects.filter(store=store)
    return render(request, "shop/product_list.html", {"products": queryset})


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
    store = request.user.merchant.store
    obj = get_object_or_404(Product.objects.filter(store=store), pk=pk)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            product = form.save(commit=False)
            album = Album()
            for file in request.FILES.getlist("pictures"):
                Picture.objects.create(attachment=file, album=album)
            album.save()
            product.edited_by = request.user
            product.save()
            return redirect(request, "shop:product_detail", pk=product.pk)
    else:
        form = ProductForm()
    return render(request, "shop/new_product.html", {"form": form})


def shop_home(request):
    queryset = Product.objects.filter(active=True)
    return render(request, "companies/shop_home.html", {"products": queryset})


def add_to_cart(request, pk):
    pass
