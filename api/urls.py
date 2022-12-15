from django.urls import path
from .views import *
path('product/', Get_product.as_view(),),
path('food/', Get_food.as_view(),),
path('rooms/', get_rooms),