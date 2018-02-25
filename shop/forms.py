from django import forms
from shop.models import Product, Order, Store


class ProductForm(forms.ModelForm):
    pictures = forms.FileField(
        required=False, widget=forms.ClearableFileInput(attrs={"multiple": True}))

    class Meta:
        model = Product
        fields = ("name", "cover_image","pictures", "description", "old_price",
                  "new_price", "quantity_in_stock", "category")


CART_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


class CartItemAddForm(forms.Form):
    quantity = forms.TypedChoiceField(
        choices=CART_QUANTITY_CHOICES, coerce=int)
    update_quantity = forms.BooleanField(
        required=False, initial=False, widget=forms.HiddenInput)


class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = ("name", "description")
