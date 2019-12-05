from django import forms
from .models import UserAccount, Cart
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):
    class Meta:
        model = UserAccount
        fields = ('username', 'first_name', 'last_name', 'email')


    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)

        if commit:
            user.save()

        user_cart = Cart(customer=user)
        user_cart.save()

        return user
