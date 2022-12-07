from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import *


@login_required(login_url='login')
def add_staff(request):
    usr = request.user
    try:
        if usr.role == 1:
            if request.method == 'POST':
                name = request.POST.get('name')
                last_name = request.POST.get('last-name')
                password = request.POST.get('password')
                confirm_password = request.POST.get('confirm-password')
                number = request.POST.get('number')
                status = request.POST.get('status')
                if confirm_password == password:
                    User.objects.create_user(
                        first_name=name, last_name=last_name,
                        password=password, number=number,
                        status=status)
                    return redirect('staff')
            else:
                return redirect('dashboard')
        elif usr.role == 3:
            if request.method == 'POST':
                name = request.POST.get('name')
                last_name = request.POST.get('last-name')
                password = request.POST.get('password')
                confirm_password = request.POST.get('confirm-password')
                number = request.POST.get('number')
                status = request.POST.get('status')
                if confirm_password == password:
                    User.objects.create_user(
                        first_name=name, last_name=last_name,
                        password=password, number=number,
                        status=status)
                    return redirect('staff')
            else:
                return redirect('dashboard')
        return render(request, 'staff/staff.html')
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
def add_category(request):
    usr = request.user
    if usr.role == 1:
        if request.method == 'POST':
            name = request.POST.get('name')
            Category.objects.create(name=name)
            return redirect('category')
    elif usr.role == 3:
        if request.method == 'POST':
            name = request.POST.get('name')
            Category.objects.create(name=name)
            return redirect('category')
    else:
        return redirect('404')


@login_required(login_url='login')
def add_food(request):
    usr = request.user
    if usr.role == 1:
        if request.method == 'POST':
            name = request.POST.get('name')
            price = request.POST.get('price')
            category = request.POST.get('category')
            available = request.POST.get('available')
            Product.objects.create(name=name, price=price, category=category, available=available)
            return redirect('food')
    elif usr.role == 3:
        if request.method == 'POST':
            name = request.POST.get('name')
            price = request.POST.get('price')
            category = request.POST.get('category')
            available = request.POST.get('available')
            Product.objects.create(name=name, price=price, category=category, available=available)
            return redirect('food')
    else:
        return redirect('404')


@login_required(login_url='login')
def add_product(request):
    user = request.user
    if user.role == 1:
        if request.method == 'POST':
            name = request.POST.get('name')
            price = request.POST.get('price')
            quantity = request.POST.get('quantity')
            category = request.POST.get('category')
            available = request.POST.get('available')
            Product.objects.create(name=name, price=price, quantity=quantity, category=category, available=available)
            return redirect('product')
    elif user.role == 3:
        if request.method == 'POST':
            name = request.POST.get('name')
            price = request.POST.get('price')
            quantity = request.POST.get('quantity')
            category = request.POST.get('category')
            available = request.POST.get('available')
            Product.objects.create(name=name, price=price, quantity=quantity, category=category, available=available)
            return redirect('product')
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
    elif usr.role == 2:
        if request.method == 'POST':
            room = request.POST.get('room')
            owner = request.POST.get('owner')
            phone = request.POST.get('phone')
            date = request.POST.get('date')
            Client.objects.create(name=owner, phone=phone)
            Order.objects.create()
