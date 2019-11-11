from django.utils import timezone
from django.db import models


# Create your models here.
class UserAccount(models.Model):
    # Fields
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(unique=True, max_length=15)
    email = models.EmailField(unique=True, max_length=100)
    password = models.CharField(max_length=30)

    # Metadata
    class Meta:
        ordering = ['last_name', 'first_name']

    # Methods
    def __str__(self):
        return self.username

    def change_first_name(self, new_name):
        self.first_name = new_name

    def change_last_name(self, new_name):
        self.last_name = new_name

    def change_email(self, new_email):
        self.email = new_email


class CustomerAccount(UserAccount):
    pass


class AdminAccount(UserAccount):
    pass


class Order(models.Model):
    # Fields
    order_number = models.IntegerField(null=False, default=00000000)
    customer = models.ForeignKey(CustomerAccount, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    total_cost = models.DecimalField(max_digits=5, decimal_places=2, null=True)

    # Metadata
    class Meta:
        ordering = ['-date']

    # Methods
    def __str__(self):
        return self.order_number

    def get_items_in_order(self):
        return InventoryItem.objects.filter(id=self.id)


class InventoryItem(models.Model):
    # Fields
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField(max_length=2000)
    orders = models.ManyToManyField("Order", blank=True)

    # Metadata
    class Meta:
        ordering = ['name']

    # Methods
    def __str__(self):
        return self.name


class Cart(models.Model):
    customer = models.OneToOneField("CustomerAccount",
                                    on_delete=models.CASCADE,
                                    null=True)


class ItemCartRelationship(models.Model):
    cart_id = models.ForeignKey("Cart", on_delete=models.CASCADE)
    item_id = models.ForeignKey("InventoryItem", on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False)