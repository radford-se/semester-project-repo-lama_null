from django import forms

from ordersystem.models import UserAccount


class UserForm(forms.ModelForm):
    class Meta:
        model = UserAccount
        widgets = {
        'password': forms.PasswordInput(),
    }