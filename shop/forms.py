from django import forms
from shop.models import Product, Order


class ProductForm(forms.ModelForm):
    pictures = forms.FileField(
        widget=forms.ClearableFileInput(attrs={"multiple": True}))

    class Meta:
        model = Product
        fields = ("name", "pictures", "description", "old_price",
                  "new_price", "quantity_in_stock", "category")
