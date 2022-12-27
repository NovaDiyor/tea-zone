from django.urls import path
from .views import *
from .change_view import *

urlpatterns = [
    path('', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('error/role', error_view, name='404'),
    path('error/password', error_password, name='error_password'),
    # Dashboard
    path('dashboard/director/', dashboard, name='dashboard'),
    path('dashboard/manager/', dashboard_manager, name='dashboard-m'),
    path('dashboard/waiter/', dashboard_waiter, name='dashboard-w'),
    path('dashboard/cooker/', dashboard_cooker, name='dashboard-c'),
    path('dashboard/call-center/', dashboard_call_center, name='dashboard-call'),
    # Templates
    path('product/', product_view, name='product'),
    path('staff/', staff_view, name='staff'),
    path('directors/', director_view, name='director'),
    path('waiters/', waiters_view, name='waiter'),
    path('managers/', manager_view, name='manager'),
    path('cookers/', cooker_view, name='cooker'),
    path('call/center/staffs/', call_center_view, name='call'),
    path('client/', client_view, name='client'),
    path('room/', room_view, name='room'),
    path('category/', category_view, name='category'),
    path('food/', food_view, name='food'),
    path('order/', order_view, name='order'),
    path('order/delivery/', delivery_view, name='delivery'),
    path('order/item/', order_item_view, name='order-item'),
    path('order/item/cooker/', order_item_cooker, name='cooker-item'),
    path('unserved-orders/', out_of_service_view, name='unserved-orders'),
    path('search/user/', search_user, name='search'),
    # Add
    path('order/add/', add_order, name='add-order'),
    path('staff/add/', add_staff, name='add-staff'),
    path('order/add/waiter/<int:pk>/', add_user_order, name='add-user-order'),
    path('order/item/add/<int:pk>/', add_order_item, name='add-order-item'),
    # Update
    path('order/update/<int:pk>/', update_order, name='update-order'),
    path('director/update/<int:pk>/', update_user, name='update-director'),
    path('category/update/<int:pk>/', update_category, name='update-category'),
    path('order/item/update/<int:pk>/', update_order_item, name='update-order-item'),
    path('product/update/<int:pk>/', update_product, name='update-product'),
    path('client/update/<int:pk>/', update_client, name='update-client'),
    path('room/update/<int:pk>/', update_room, name='update-room'),
    path('food/update/<int:pk>/', update_food, name='update-food'),
    path('food/change/<int:pk>/', change_food, name='change-food'),
    # Delete
    path('user/delete/<int:pk>/', delete_user, name='delete-user'),
    path('room/delete/<int:pk>/', delete_room, name='delete-room'),
    path('order/delete/<int:pk>/', delete_order, name='delete-order'),
    path('order/item/delete/<int:pk>/', delete_order_item, name='delete-order-item'),
    path('category/delete/<int:pk>/', delete_category, name='delete-category'),
    path('product/delete/<int:pk>/', delete_product, name='delete-product'),
    path('food/delete/<int:pk>/', delete_food, name='delete-food'),
]
