from django import forms
from .models import UserAccount, Cart
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):
    class Meta:
        model = UserAccount
        fields = ('username', 'first_name', 'last_name', 'email')


    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user_cart = Cart(customer=user.id)
        user_cart.save()

        if commit:
            user.save()

        return user
