from django.contrib import admin
from shop.models import Picture,Order,OrderItem,Merchant,Store,Product,Category,Album

# Register your models here.
admin.site.register(Picture)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Merchant)
admin.site.register(Store)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Album)
