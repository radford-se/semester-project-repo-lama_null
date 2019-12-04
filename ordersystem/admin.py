from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from ordersystem.models import Order,\
    CustomerAccount, AdminAccount,\
    InventoryItem, Cart, Category

# Register your models here.
admin.site.register(CustomerAccount)
admin.site.register(AdminAccount)
admin.site.register(Cart)
admin.site.register(Category)
admin.site.register(InventoryItem)

@admin.register(Order)
class ViewAdmin(ImportExportModelAdmin):
    pass