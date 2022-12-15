from django.urls import path
from .views import *

urlpatterns = [
    path('product/', Get_product.as_view(),),
    path('food/', Get_food.as_view(),),
    path('rooms/', get_rooms),
    path('create-order/', create_order),
    path('info/', get_info),
    path('detail/', get_detail),
]
