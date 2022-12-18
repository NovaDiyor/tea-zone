from datetime import date, datetime
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import *


def delete_manager(request, pk):
    usr = request.user
    if usr.role == 1:
        if request.method == 'POST':
            password = request.POST.get('password')
            if usr.password == password:
                User.objects.get(id=pk).delete()
                return redirect('manager')
            else:
                return redirect('404')
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


def delete_order_item(request, pk):
    item = OrderItem.objects.get(id=pk)
    order = item.order
    if item.product:
        order.bill -= item.product.price * item.quantity
    elif item.food:
        order.bill -= item.food.price * item.quantity
    order.save()
    item.delete()
    return redirect('order-item')


def delete_order(request, pk):
    Order.objects.get(id=pk).delete()
    return redirect('order')


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
        if food.available == True:
            food.available = False
        else:
            food.available = True
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
        for i in item:
            order.bill += i.food.price * i.quantity
        order.save()
        context = {
            'order': order,
            'item': item,
        }
        return render(request, 'order.html', context)
    elif usr.role == 5:
        Order.objects.get(id=pk).delete()
        return redirect('order')
    else:
        return redirect('404')


def update_director(request, pk):
    director = User.objects.get(id=pk)
    if request.method == 'POST':
        name = request.POST.get('name')
        l_name = request.POST.get('l-name')
        phone = request.POST.get('phone')
        director.first_name = name
        director.last_name = l_name
        director.number = phone
        director.save()
        return redirect('director')


def update_order(request, pk):
    order = Order.objects.get(id=pk)
    if order.done == False:
        order.done = True
        order.room.busy = False
        order.room.save()
        order.save()
    elif order.done == True:
        order.done = False
        order.room.busy = True
        order.room.save()
        order.save()
    return redirect('order')


def update_order_item(request, pk):
    item = OrderItem.objects.get(id=pk)
    if request.method == 'POST':
        order = request.POST.get('order')
        food = request.POST.get('food')
        product = request.POST.get('product')
        quantity = request.POST.get('quantity')
        item.order_id = order


def update_food(request,pk):
    user = request.user
    if user.role == 1:
        if request.method == 'POST':
            f = Food.objects.get(id=pk)
            price = request.POST.get('price')
            f.price = price
            f.save()
            return redirect('food')
        return render(request,'food-update.html')
    elif user.role == 3:
        if request.method == 'POST':
            f = Food.objects.get(id=pk)
            price = request.POST.get('price')
            f.price = price
            f.save()
            return redirect('food')
        return render(request, 'food-update.html')
    else:
        return redirect('404')


def update_product(request, pk):
    user = request.user
    if request.method == 'POST':
        pr = Product.objects.get(id=pk)
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')
        if price:
            pr.price = price
        else:
            pr.price = pr.price
        if int(quantity) < 0:
            quantity = 0
        pr.quantity = quantity
        pr.save()
        return redirect('product')


@login_required(login_url='login')
def update_client(request, pk):
    client = Client.objects.get(id=pk)
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        client.name = name
        client.phone = phone
        client.save()
        return redirect('client')
    return render(request, 'staff/client.html')



