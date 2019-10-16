from django.db import models


# Create your models here.
class OrderSystem(models.Model):
    """A typical class defining a model, derived from the Model class."""

    # Fields
    name = models.CharField(max_length=20)
    # customer = models.ForeignKey('UserAccount')
    order = models.ForeignKey('Order')

    # Metadata
    class Meta:
        ordering = ['name']

    # Methods
    def get_absolute_url(self):
        """Returns the url to access a particular instance of MyModelName."""
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.my_field_name


class UserAccount(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(unique=True, max_length=15)
    email = models.EmailField(unique=True, max_length=100)
    password = models.CharField(max_length=30)

    class Meta:
        ordering = ['last_name']

    def __str__(self):
        return self.username


class CustomerAccount(UserAccount):
    order = models.ForeignKey('Order')
    favorite_item = models.ForeignKey('InventoryItem')
    favorite_order = models.ForeignKey('Order')


class AdminAccount(UserAccount):
    pass


class InventoryItem(models.Model):
    name = models.CharField(max_length=100)