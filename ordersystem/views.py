# Create your views here.
from django.contrib import messages
from django.contrib.auth import authenticate, logout, update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from .models import InventoryItem, Order, Cart
from django.views.generic.base import View


def index(request):
    return render(request, 'index.html', {})


def login(request):
    return render(request, 'login.html', {})


def logout_user(request):
    logout(request)
    return redirect('../')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            return redirect('../thankyou')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


@login_required()
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully changed.')
            return redirect('change_password')
        else:
            messages.error(request, 'Error in input, please fix')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'registration/change_password.html', {'form': form})


def ordering_page(request):
    return render(request, 'ordering_page.html', {})


def thankyou(request):
    return render(request, 'thankyou.html', {})


class InventoryView(View):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        all_items = InventoryItem.objects.all()

        context["menu_items"] = all_items
        context["test"] = "test"

        return context


class OrderListView(ListView):
    context_object_name = 'orders'
    model = Order


class CartListView(ListView):
    context_object_name = 'cart'
    model = Cart

class ItemListView(ListView):
    context_object_name = 'items'
    model = InventoryItem
