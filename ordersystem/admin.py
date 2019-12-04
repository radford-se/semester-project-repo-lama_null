from django.contrib import admin
from ordersystem.models import Order,UserAccount, AdminAccount, InventoryItem, Cart, Category

# Register your models here.
admin.site.register(UserAccount)
admin.site.register(Order)
admin.site.register(InventoryItem)
admin.site.register(Cart)
admin.site.register(Category)
