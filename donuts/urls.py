from django.contrib import admin
from django.urls import path, include
from ordersystem import views

app_name = 'ordersystem'
urlpatterns = [
    path('ordersystem/', include('ordersystem.urls')),
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
    path('accounts/view_cart/', views.payment_page.as_view(), name='paypage'),
    path('accounts/view_cart/confirmation/', views.charge, name='confirmation'),
]
