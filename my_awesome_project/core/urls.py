from django.urls import path

from .views import create_orders_api_view, get_list_api_view

urlpatterns = [path("orders/", get_list_api_view), path("orders/create", create_orders_api_view)]
