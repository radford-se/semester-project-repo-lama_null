# Create your views here.
import stripe

from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, logout, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import InventoryItem, Category, Order, ItemCartRelationship, Cart
from django.views.generic.base import View, TemplateView
from .forms import RegisterForm

stripe.api_key = settings.STRIPE_SECRET_KEY


def index(request):
    return render(request, 'index.html', {})


def login(request):
    return render(request, 'login.html', {})


def logout_user(request):
    logout(request)
    return redirect('../accounts/login')


def ordering_page(request):
    items = InventoryItem.objects.all()
    categories = Category.objects.all()
    return render(request, 'ordering_page.html', {'items': items, 'categories': categories, })


def button(request):
    return render(request,'ordering_page.html')


def add_to_cart(request, inventory_item_id):
    item1 = get_object_or_404(InventoryItem, pk=inventory_item_id)
    cart = get_object_or_404(Cart, customer=request.user.id)
    # if request.user.is_authenticated():
    #     cart = request.user.cart_id
    # else:
    #     cart = None
    item = ItemCartRelationship(
        cart_id=cart,
        item_id=item1)
    item.save()
    return render(request, 'ordering_page.html') #, {'item': item})


def signup(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            return redirect('../thankyou')
    else:
        form = RegisterForm()
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


class payment_page(TemplateView):
    template_name = 'view_cart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['key'] = settings.STRIPE_PUBLISHABLE_KEY
        return context


def charge(request):
    if request.method == 'POST':
        charge = stripe.Charge.create(
            amount=500,
            currency='usd',
            description='A Django charge',
            source=request.POST['stripeToken']
        )
    return render(request, 'payment_confirmation.html')


def favorites(request):
    return render(request, 'favorites.html',{})


def recent_orders(request):
    orders = Order.objects.all()
    items = InventoryItem.objects.all()
    return render(request, 'recent_orders.html', {"orders": orders, "items": items})


def view_cart(request):
    cart = ItemCartRelationship.objects.all()
    return render(request, 'view_cart.html', {"cart": cart})


