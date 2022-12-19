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
    Category.objects.get(id=pk).delete()
    return redirect('category')


def change_food(request, pk):
    food = Food.objects.get(id=pk)
    if food.available == True:
        food.available = False
    else:
        food.available = True
    food.save()
    return redirect('food')


def delete_food(request, pk):
    Food.objects.get(id=pk).delete()
    return redirect('food')


def delete_product(request, pk):
    Product.objects.get(id=pk).delete()
    return redirect('product')


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
        return render(request, 'product/order.html', context)
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


def update_category(request, pk):
    category = Category.objects.get(id=pk)
    if request.method == 'POST':
        name = request.POST.get('name')
        category.name = name
        category.save()
        return redirect('category')


def update_room(request, pk):
    room = Rooms.objects.get(id=pk)
    if request.method == 'POST':
        number = request.POST.get('number')
        place = request.POST.get('place')
        room.number = number
        room.places = place
        room.save()
        return redirect('room')


def update_order_item(request, pk):
    item = OrderItem.objects.get(id=pk)
    if request.method == 'POST':
        order_id = request.POST.get('order')
        food_id = request.POST.get('food')
        product_id = request.POST.get('product')
        quantity = request.POST.get('quantity')
        item.order_id = order_id
        if food_id == 'None':
            pro_get = Product.objects.get(id=product_id)
            product = item.product
            item_quantity = int(item.quantity)
            product.quantity += item_quantity
            if int(quantity) > pro_get.quantity:
                quantity = pro_get.quantity
            pro_get.quantity -= int(quantity)
            pro_get.save()
            product.save()
            item.product = pro_get
            item.food = None
            item.quantity = quantity
            item.save()
        if product_id == 'None':
            order = Order.objects.get(id=order_id)
            food_get = Food.objects.get(id=food_id)
            food = item.food
            item_quantity = int(item.quantity)
            order.bill -= food.price * item_quantity
            order.bill += food_get.price * int(quantity)
            order.save()
            item.product = None
            item.food = food_get
            item.quantity = quantity
            item.save()
        return redirect('order-item')


def update_food(request, pk):
    f = Food.objects.get(id=pk)
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        category = request.POST.get('category')
        f.name = name
        f.price = price
        f.category_id = category
        f.save()
        return redirect('food')


def update_product(request, pk):
    if request.method == 'POST':
        pr = Product.objects.get(id=pk)
        name = request.POST.get('name')
        category = request.POST.get('category')
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')
        if name:
            pr.name = name
        else:
            pr.name = name
        if category:
            pr.category_id = category
        else:
            pr.category = category
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



