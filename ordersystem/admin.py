from django.contrib import admin
from ordersystem.models import Order, CustomerAccount, AdminAccount, InventoryItem, Cart

# Register your models here.
admin.site.register(Order)
admin.site.register(CustomerAccount)
admin.site.register(AdminAccount)
admin.site.register(InventoryItem)
admin.site.register(Cart)