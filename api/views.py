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
        food = Food.objects.filter(is_yes=True)
        foods = []
        for i in food:
            data = {
                'name': i.name,
                'price': i.price,
                'category': i.category

            }
            foods.append(data)
            return Response(foods)


@api_view(['POST'])
def get_rooms(request):
    date = request.POST['date']
    order = Order.objects.filter(done=False, date=date)
    room = []
    if order:
        for x in Rooms.objects.all():
            for i in order:
                if x == i.room:
                    pass
                else:
                    if x in room:
                        pass
                    else:
                        room.append(x)
    else:
        for i in Rooms.objects.all():
            room.append(i)
    return Response(Rooms_serializer(room, many=True).data)


@api_view(['POST'])
def client_create(request):
    name = request.POST.get('name')
    number = request.POST.get('number')
    Client.objects.create(name=name, number=number)
    return Response('')

import datetime

@api_view(['POST'])
def create_order(request):
    try:
        name = request.POST.get("name")
        room = request.POST.get('room')
        phone = request.POST.get('phone')
        date = request.POST.get("date")
        if Client.objects.filter(phone=phone).count() == 0:
            client = Client.objects.create(name=name, phone=phone)
        else:
            client = Client.objects.get(phone=phone)
        r = Rooms.objects.get(number=room)
        r.busy = True
        r.save()
        Order.objects.create(
            room=Rooms.objects.get(number=room),
            delivery=False,
            owner=client,
            date=date
        )
        return Response({"status": 200})
    except Exception as err:
        return Response({"status": 500})


@api_view(['POST'])
def create_delivery(request):
    try:
        name = request.POST.get("name")
        room = request.POST.get('room')
        phone = request.POST.get('phone')
        date = request.POST.get("date")
        if Client.objects.filter(phone=phone).count() == 0:
            client = Client.objects.create(name=name, phone=phone)
        else:
            client = Client.objects.get(phone=phone)
        r = Rooms.objects.get(number=room)
        r.is_yes = True
        r.save()
        Order.objects.create(
            room=Rooms.objects.get(number=room),
            delivery=False,
            owner=client,
            date=date
        )
        return Response({"status": 200})
    except Exception as err:
        return Response({"status": 500})


@api_view(['GET'])
def get_info(request):
    info = Bot.objects.last()
    return Response(BotInfoSerializer(info).data)


@api_view(['GET'])
def get_detail(request):
    info = BotDetail.objects.last()
    return Response(BotDetailSerializer(info).data)

