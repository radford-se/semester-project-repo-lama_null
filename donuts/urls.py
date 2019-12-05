"""donuts URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from ordersystem import views
from ordersystem.models import InventoryItem, Order, Category

app_name = 'ordersystem'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.index, name='index'),
    path('accounts/login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('ordering_page/', views.ordering_page, name='ordering_page'),
    path('logout/', views.logout_user, name='logout'),
    path('thankyou/', views.thankyou, name='thankyou'),
    path('accounts/change_password/', views.change_password, name='change_password'),
    path('accounts/settings/', views.change_settings, name='change_settings'),
    path('ordering_page/<int:inventory_item_id>/', views.add_to_cart, name='add_to_cart'),
    path('accounts/recent_orders/', views.recent_orders, name='recent_orders'),
    path('accounts/favorites/', views.favorites, name='favorites'),
    path('accounts/view_cart/', views.view_cart, name='view_cart'),
    path('payments/', views.payment_page.as_view(), name='paypage'),
    path('payments/confirmation/', views.charge, name='confirmation'),
]

urlpatterns += [
    path('ordersystem/', include('ordersystem.urls')),
]
