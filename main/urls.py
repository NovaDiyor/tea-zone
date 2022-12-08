from django.urls import path
from .views import *
from .change_view import *

urlpatterns = [
    path('', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('error/role', error_view, name='404'),
    path('dashboard/director/', dashboard, name='dashboard'),
    path('dashboard/manager/', dashboard_manager, name='dashboard-m'),
    path('dashboard/waiter/', dashboard_waiter, name='dashboard-w'),
    path('dashboard/cooker/', dashboard_cooker, name='dashboard-c'),
    path('dashboard/call-center/', dashboard_call_center, name='dashboard-call'),
    path('product/', product_view, name='product'),
    path('directors/', director_view, name='director'),
    path('waiters/', waiters_view, name='waiter'),
    path('managers/', manager_view, name='manager'),
    path('cookers/', cooker_view, name='cooker'),
    path('call/canter/staffs/', call_center_view, name='call'),
    path('staff/add/', add_staff, name='add-staff'),
    path('room/', room_view, name='room'),
    path('category/', category_view, name='category'),
    path('food/', food_view, name='food'),
    path('order/', order_view, name='order'),
    path('order/item', order_item_view, name='order-item'),
    path('user/delete/', delete_manager, name='delete-user'),
    path('room/delete/', delete_room, name='delete-room'),
    path('category/delete/', delete_category, name='delete-category'),
    path('food/change/', change_food, name='change-food'),
    path('waiters/add/', delete_product, name='delete-product'),
    path('order/change/', change_order, name='change-order'),
]
