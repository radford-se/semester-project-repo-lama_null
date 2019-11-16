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
from ordersystem.models import InventoryItem, Order
from ordersystem.views import ItemListView, OrderListView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.index, name='index'),
    path('accounts/login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('ordering_page/', ItemListView.as_view(), name='ordering_page'),
    path('logout/', views.logout_user, name='logout'),
    path('thankyou/', views.thankyou, name='thankyou'),
    path('accounts/change_password/', views.change_password, name='change_password'),
    path('orders/', OrderListView.as_view(), name='orders'),
]

urlpatterns += [
    path('ordersystem/', include('ordersystem.urls')),
]

item_list = {
    'queryset' : InventoryItem.objects.all(),
    'template_name' : 'ordering_page.html/'
}
order_list = {
    'queryset' : Order.objects.all(),
}
# cart_list = {
#     'queryset' : Cart.objects.all(),
# }