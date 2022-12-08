from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import *


@login_required(login_url='login')
def add_staff(request):
    usr = request.user
    print(usr)
    try:
        if usr.role == 1:
            if request.method == 'POST':
                username = request.POST.get('username')
                name = request.POST.get('name')
                last_name = request.POST.get('last-name')
                password = request.POST.get('password')
                confirm_password = request.POST.get('cp')
                number = request.POST.get('number')
                status = request.POST.get('status')
                if confirm_password == password:
                    User.objects.create_user(
                        username=username, first_name=name,
                        last_name=last_name, password=password,
                        number=number, role=status)
                    return redirect('add-staff')
            else:
                return render(request, 'staff/add-staff.html')
        elif usr.role == 3:
            print('hello')
            if request.method == 'POST':
                print('bye')
                username = request.POST.get('username')
                name = request.POST.get('name')
                last_name = request.POST.get('last-name')
                password = request.POST.get('password')
                cp = request.POST.get('cp')
                number = request.POST.get('number')
                status = request.POST.get('status')
                if cp == password:
                    print('hello')
                    User.objects.create_user(
                        username=username, first_name=name,
                        last_name=last_name, password=password,
                        number=number, role=status)
                    return redirect('add-staff')
            else:
                return render(request, 'staff/add-staff.html')
        return redirect('404')
    except Exception as err:
        print(err)


@login_required(login_url='login')
def add_room(request):
    usr = request.user
    if usr.role == 1:
        if request.method == 'POST':
            number = request.POST.get('number')
            place = request.POST.get('place')
            Rooms.objects.create(number=number, places=place)
            return redirect('room')
    elif usr.role == 3:
        if request.method == 'POST':
            number = request.POST.get('number')
            place = request.POST.get('place')
            Rooms.objects.create(number=number, places=place)
            return redirect('room')
    else:
        return redirect('404')


@login_required(login_url='login')
def add_order(request):
    usr = request.user
    if usr.role == 5:
        if request.method == 'POST':
            user = request.POST.get('user')
            room = request.POST.get('room')
            owner = request.POST.get('owner')
            phone = request.POST.get('phone')
            address = request.POST.get('address')
            date = request.POST.get('date')
            delivery_date = request.POST.get('delivery-date')
            delivery = request.POST.get('delivery')
            if delivery is None:
                delivery = False
                delivery_date = None
                address = None
            else:
                room = None
            Client.objects.create(name=owner, phone=phone)
            client = Client.objects.last()
            Order.objects.create(user_id=user, room_id=room, address=address, date=date, delivery_date=delivery_date, owner=client, phone=client.phone, delivery=delivery)
    elif usr.role == 2:
        if request.method == 'POST':
            room = request.POST.get('room')
            owner = request.POST.get('owner')
            phone = request.POST.get('phone')
            date = request.POST.get('date')
            Client.objects.create(name=owner, phone=phone)
            client = Client.objects.last()
            Order.objects.create(room_id=room, owner=client, date=date, user_id=usr)
    else:
        return redirect('404')


@login_required(login_url='login')
def add_order_item(request):
    usr = request.user
    if usr.role == 5:
        if request.method == 'POST':
            order = request.POST.get('order')
            food = request.POST.get('food')
            product = request.POST.get('product')
            quantity = request.POST.get('quantity')
            if food:
                product = None
            elif product:
                food = None
            OrderItem.objects.create(order_id=order, food_id=food, product_id=product, quantity=quantity)
            return redirect('order-item')
    elif usr.role == 2:
        if request.method == 'POST':
            order = request.POST.get('order')
            food = request.POST.get('food')
            product = request.POST.get('product')
            quantity = request.POST.get('quantity')
            if food:
                product = None
            elif product:
                food = None
            OrderItem.objects.create(order_id=order, food_id=food, product_id=product, quantity=quantity)
            return redirect('order-item')
    else:
        return redirect('404')
