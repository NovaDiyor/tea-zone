from django.shortcuts import render, redirect
from .models import *


def delete_user(request, pk):
    usr = request.user
    if usr.role == 1:
        User.objects.get(id=pk).delete()
        return redirect('staff')
    elif usr.role == 3:
        User.objects.get(id=pk).delete()
        return redirect('staff')
    else:
        return redirect('404')


def delete_room(request, pk):
    usr = request.user
    if usr.role == 1:
        Rooms.objects.get(id=pk).delete()
        return redirect('room')
    elif usr.role == 3:
        Rooms.objects.get(id=pk).delete()
        return redirect('room')
    else:
        return redirect('404')


def delete_category(request, pk):
    usr = request.user
    if usr.role == 1:
        Category.objects.get(id=pk).delete()
        return redirect('category')
    elif usr.role == 3:
        Category.objects.get(id=pk).delete()
        return redirect('category')
    else:
        return redirect('404')


def change_food(request, pk):
    usr = request.user
    if usr.role == 1:
        Food.objects.get(id=pk).delete()
        return redirect('food')
    elif usr.role == 3:
        Food.objects.get(id=pk).delete()
        return redirect('food')
    elif usr.role == 4:
        food = Food.objects.get(id=pk)
        food.available = False
        food.save()
        return redirect('food')
    else:
        return redirect('404')


def delete_product(request, pk):
    usr = request.user
    if usr.role == 1:
        Product.objects.get(id=pk).delete()
        return redirect('product')
    elif usr.role == 3:
        Product.objects.get(id=pk).delete()
        return redirect('product')
    elif usr.role == 4:
        pro = Product.objects.get(id=pk)
        pro.quantity = 0
        pro.available = False
        pro.save()
        return redirect('product')
    else:
        return redirect('404')


def change_order(request, pk):
    usr = request.user
    if usr.role == 2:
        order = Order.objects.get(id=pk)
        order.done = True
        item = OrderItem.objects.filer(order=order)
        total = 0
        for i in item:
            total += i.food.price * i.quantity
        bill = total
        return render(request, 'order.html', bill)
    elif usr.role == 5:
        Order.objects.get(id=pk).delete()
        return redirect('order')
    else:
        return redirect('404')
