from django.utils import timezone
from django.db import models


# Create your models here.
class OrderSystem(models.Model):
    # Fields
    name = models.CharField(max_length=20)
    customer = models.ForeignKey('UserAccount', on_delete=models.CASCADE)
    order = models.ForeignKey('Order', on_delete=models.CASCADE)

    # Metadata
    class Meta:
        ordering = ['name']

    # Methods
    def get_absolute_url(self):
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        return self.my_field_name


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


class CustomerAccount(UserAccount):
    pass


class AdminAccount(UserAccount):
    pass


class InventoryItem(models.Model):
    # Fields
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    inventory_count = models.IntegerField()
    description = models.TextField(max_length=2000)

    # Metadata
    class Meta:
        ordering = ['name']

    # Methods
    def __str__(self):
        return self.name


class Order(models.Model):
    # Fields
    order_number = models.IntegerField(null=False, default=00000000)
    customer = models.ForeignKey(CustomerAccount, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now())

    # Metadata
    class Meta:
        ordering = ['-date']

    # Methods
    def __str__(self):
        return self.order_number
