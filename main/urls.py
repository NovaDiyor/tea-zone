from django.urls import path
from .views import *
from .change_view import *
from .add_view import *

urlpatterns = [
    path('', login_view, name='login'),
    path('error/role', error_view, name='404'),
    path('dashboard/director/', dashboard, name='dashboard'),
    path('dashboard/manager/', dashboard_manager, name='dashboard-m'),
    path('dashboard/waiter/', dashboard_waiter, name='dashboard-w'),
    path('dashboard/cooker/', dashboard_cooker, name='dashboard-c'),
    path('dashboard/call-center/', dashboard_call_center, name='dashboard-call'),
    path('product/', product_view, name='product'),
    path('waiters/', waiters_view, name='waiter'),
    path('waiters/add/', add_staff, name='add-staff'),
    path('rooms/add/', add_room, name='add-room'),
    path('category/add/', add_category, name='add-category'),
    path('food/add/', add_food, name='add-food'),
    path('user/delete/', delete_user, name='delete-user'),
    path('room/delete/', delete_room, name='delete-room'),
    path('category/delete/', delete_category, name='delete-category'),
    path('food/change/', change_food, name='change-food'),
    path('waiters/add/', delete_product, name='delete-product'),
    path('order/change/', change_order, name='change-order'),
]
