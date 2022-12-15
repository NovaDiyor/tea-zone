from django.shortcuts import render
from.serializer import *
from main.models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView




class Get_product(APIView):
    def get(self,request):
        product = Product.objects.filter(available=True)
        products = []
        for i in product:
            data = {
                'name': i.name,
                'price': i.price,
                'category': i.category

            }
            products.append(data)
            return Response(products)


class Get_food(APIView):
    def get(self,request):
        food = Food.objects.filter(available=True)
        foods = []
        for i in food:
            data = {
                'name': i.name,
                'price': i.price,
                'category': i.category

            }
            foods.append(data)
            return Response(foods)

@api_view('GET')
def get_rooms(request):
    room = Rooms.objects.filter(busy=True)
    rooms = []
    for i in room:
        data = {
            'number':i.number,
            'places':i.places
        }
        rooms.append(data)
        return Response(Rooms_serializer (room,many=True).data)



@api_view(['POST'])
def client_create(request):
    name = request.POST.get('name')
    number = request.POST.get('number')
    Client.objects.create(name=name,number=number)
    return Response()


