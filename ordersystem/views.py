# Create your views here.
from django.contrib import messages
from django.contrib.auth import authenticate, logout, update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from .models import InventoryItem, Order, Cart, Category, ItemCartRelationship
from django.views.generic.base import View
from django.shortcuts import get_object_or_404, render


def index(request):
    return render(request, 'index.html', {})


def login(request):
    return render(request, 'login.html', {})


def logout_user(request):
    logout(request)
    return redirect('../')


def button(request):
    return render(request,'ordering_page.html')


def add_to_cart(request, inventory_item_id):
    item = get_object_or_404(InventoryItem, pk=inventory_item_id)
    if request.user.is_authenticated():
        cart = request.user.cart_id
    else:
        cart = None
    item = ItemCartRelationship.create(
        cart_id=cart,
        item_id=item.id)
    item.save()
    return render(request, 'ordering_page.html', {'item': item})


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


@login_required()
def change_settings(request):
    return render(request, 'registration/settings.html')


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


class CategoryListView(ListView):
    context_object_name = 'categories'
    model = Category

    def get_context_data(self, **kwargs):
        context = Category.name
        return context


