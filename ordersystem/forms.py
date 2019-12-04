from django import forms
from .models import UserAccount
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):
    class Meta:
        model = UserAccount
        fields = ('username', 'first_name', 'last_name', 'email')

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)

        if commit:
            user.save()

        return user

#
# class UserForm(forms.ModelForm):
#     class Meta:
#         model = UserAccount
#         widgets = {'password': forms.PasswordInput()}
#         fields = ['username',
#                   'first_name',
#                   'last_name',
#                   'email',
#                   'password']
#
#     def save(self, commit=True):
#         user = super(UserForm, self).save(commit=False)
#         user.username = ['username']
#         user.first_name = ['first_name']
#         user.last_name = ['last_name']
#         user.email = ['email']
