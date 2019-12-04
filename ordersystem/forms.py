from django import forms
from ordersystem.models import UserAccount
from django.contrib.auth.forms import UserCreationForm


class UserForm(forms.ModelForm):
    class Meta:
        model = UserAccount
        widgets = {'password': forms.PasswordInput()}


class SignUpForm(UserCreationForm):
    class Meta:
        model = UserAccount
        fields = ('username',
                  'first_name',
                  'last_name',
                  'email',
                  'password1',
                  'password2')

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.first_name = ['first_name']
