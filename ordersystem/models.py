from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models


class InventoryItem(models.Model):
    # Fields
    name = models.CharField(max_length=27)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField(max_length=2000)
    orders = models.ManyToManyField("Order", blank=True)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)

    # Metadata
    class Meta:
        ordering = ['name']

    # Methods
    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class Cart(models.Model):
    customer = models.OneToOneField("UserAccount",
                                    on_delete=models.CASCADE,
                                    null=True)


class AccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("You must have an email associated with your account")
        if not username:
            raise ValueError("You must have a username associated with your account")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None, first_name=None, last_name=None):
        if not email:
            raise ValueError('You must have an email associated with your account')
        if not username:
            raise ValueError('You must have a username associated with your account')
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


# Create your models here.
class UserAccount(AbstractBaseUser):
    # Fields
    username = models.CharField(verbose_name='username', unique=True, max_length=15)
    email = models.EmailField(unique=True, max_length=100)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = AccountManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email']

    # Metadata
    class Meta:
        ordering = ['last_name', 'first_name']

    # Methods
    def __str__(self):
        return self.username

    def __unicode__(self):
        return self.username

    def change_first_name(self, new_name):
        self.first_name = new_name

    def change_last_name(self, new_name):
        self.last_name = new_name

    def change_email(self, new_email):
        self.email = new_email

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser


class Order(models.Model):
    # Fields
    order_number = models.IntegerField(null=False, default=00000000)
    customer = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    total_cost = models.DecimalField(max_digits=5, decimal_places=2, null=True)

    # Metadata
    class Meta:
        ordering = ['-date']

    # Methods
    def __str__(self):
        return self.order_number.__str__()


class ItemCartRelationship(models.Model):
    cart_id = models.ForeignKey("Cart", on_delete=models.CASCADE)
    item_id = models.ForeignKey("InventoryItem", on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=1)


class Category(models.Model):
    name = models.CharField(default="Miscellaneous", max_length=30)

    # Methods
    class Meta:
        verbose_name_plural = "categories"
        ordering = ["name"]

    def __str__(self):
        return self.name
