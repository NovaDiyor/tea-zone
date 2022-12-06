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
        return render(request, 'add-staff.html')
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
            return redirect('add-room')
    elif usr.role == 3:
        if request.method == 'POST':
            number = request.POST.get('number')
            place = request.POST.get('place')
            Rooms.objects.create(number=number, places=place)
            return redirect('add-room')
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
            return redirect('product')
    elif usr.role == 3:
        if request.method == 'POST':
            name = request.POST.get('name')
            price = request.POST.get('price')
            category = request.POST.get('category')
            available = request.POST.get('available')
            Product.objects.create(name=name, price=price, category=category, available=available)
            return redirect('product')
    else:
        return redirect('404')
