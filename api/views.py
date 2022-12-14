from django.shortcuts import render
from.serializer import *
from main.models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView




# class Get_product(APIView):
#     def get(self,request):
#         product = Product.objects.filter(available=True)
#         products = []
#         for i in product:
#             data = {
#
#             }



