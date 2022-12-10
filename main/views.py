from datetime import date
from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def login_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        number = request.POST.get('number')
        if number is None:
            number = 1
        user = User.objects.filter(username=name)
        if user.count() > 0:
            usr = authenticate(username=name, password=password)
            if usr is not None:
                login(request, usr)
                return redirect('dashboard')
            else:
                return redirect('404')
        else:
            user = User.objects.filter(number=number)
            if user.count() > 0:
                usr = authenticate(number=number, password=password)
                if usr:
                    login(request, usr)
                    return redirect('dashboard')
                else:
                    return redirect('404')
            return redirect('login')
    return render(request, 'login.html')


@login_required(login_url='login')
def logout_view(request):
    logout(request)
    return redirect('login')


def error_view(request):
    return render(request, '404.html')


@login_required(login_url='login')
def add_staff(request):
    usr = request.user
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
            if request.method == 'POST':
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
def dashboard_waiter(request):
    usr = request.user
    if usr.role == 2:
        day = date.today()
        order = Order.objects.filter(done=True, date__day=day.day, user=usr)
        month = Order.objects.filter(done=True, date__month=day.month, user=usr)
        proces = Order.objects.filter(done=False, date__day=day.day, user=usr)
        total = 0
        for i in order:
            item = OrderItem.objects.get(order=i)
            total += item.quantity * item.price % 8
        context = {
            'total': total,
            'done': order.count(),
            'in_proces': proces.count(),
            'month': month.count(),
        }
        return render(request, 'dashboard/dashboard-waiter.html', context)
    else:
        return redirect('dashboard')


@login_required(login_url='login')
def dashboard_manager(request):
    usr = request.user
    if usr.role == 3:
        return render(request, 'dashboard/dashboard-manager.html')
    else:
        return redirect('dashboard')


@login_required(login_url='login')
def dashboard_cooker(request):
    usr = request.user
    if usr.role == 4:
        return render(request, 'dashboard/dashboard-cooker.html')
    else:
        return redirect('dashboard')


@login_required(login_url='login')
def dashboard_call_center(request):
    usr = request.user
    if usr.role == 5:
        return render(request, 'dashboard/dashboard-call.html')
    else:
        return redirect('dashboard')


@login_required(login_url='login')
def dashboard(request):
    usr = request.user
    if usr.role == 1:
        client = Client.objects.all()
        staff = User.objects.all()
        order = Order.objects.filter(done=True)
        total = 0
        revenue = 0
        for i in order:
            item = OrderItem.objects.get(order=i)
            total += item.quantity * item.price
            for x in staff:
                revenue += total - x.salary
        context = {
            'client': client.count(),
            'staff': staff.count(),
            'total': total,
            'revenue': revenue
        }
        return render(request, 'dashboard/dashboard.html', context)
    elif usr.role == 2:
        return redirect('dashboard-w')
    elif usr.role == 3:
        return redirect('dashboard-m')
    elif usr.role == 4:
        return redirect('dashboard-c')
    elif usr.role == 5:
        return redirect('dashboard-call')
    else:
        return redirect('404')


@login_required(login_url='login')
def manager_view(request):
    usr = request.user
    if usr.role == 1:
        context = {
            'manager': User.objects.filter(role=3)
        }
        return render(request, 'staff/manager.html', context)
    elif usr.role == 3:
        context = {
            'manager': User.objects.filter(role=3)
        }
        return render(request, 'staff/manager.html', context)
    else:
        return redirect('404')


@login_required(login_url='login')
def cooker_view(request):
    usr = request.user
    if usr.role == 1:
        cookers = User.objects.filter(role=4)
        context = {
            'cooker': cookers
        }
        return render(request, 'staff/cooker.html', context)
    elif usr.role == 3:
        cookers = User.objects.filter(role=4)
        context = {
            'cooker': cookers
        }
        return render(request, 'staff/cooker.html', context)
    else:
        return redirect('404')


@login_required(login_url='login')
def director_view(request):
    user = request.user
    if user.role == 1:
        context = {
            'total': User.objects.filter(role=1).count(),
            'director': User.objects.filter(role=1),
        }
        return render(request, 'staff/director.html', context)
    elif user.role == 3:
        context = {
            'total': User.objects.filter(role=1).count(),
            'director': User.objects.filter(role=1),
        }
        return render(request, 'staff/director.html', context)
    else:
        return redirect('404')


@login_required(login_url='login')
def waiters_view(request):
    user = request.user
    if user.role == 1:
        waiter = User.objects.filter(role=2)
        context = {
            'waiters': waiter,
        }
        return render(request, 'staff/waiter.html', context)
    elif user.role == 3:
        waiter = User.objects.filter(role=2)
        context = {
            'waiters': waiter,
        }
        return render(request, 'staff/waiter.html', context)
    else:
        return redirect('404')


@login_required(login_url='login')
def call_center_view(request):
    usr = request.user
    if usr.role == 1:
        context = {
            'call_canter': User.objects.filter(role=5)
        }
        return render(request, 'staff/call-canter.html', context)
    elif usr.role == 3:
        context = {
            'call_center': User.objects.filter(role=5)
        }
        return render(request, 'staff/call-canter.html', context)
    else:
        return redirect('404')


@login_required(login_url='login')
def client_view(request):
    context = {
        'client': Client.objects.all()
    }
    return render(request, 'staff/client.html', context)


@login_required(login_url='login')
def product_view(request):
    pro = Product.objects.all()
    context = {
        'product': pro,
        'category': Category.objects.all()
    }
    for i in pro:
        if i.quantity <= 0:
            i.available = False
        else:
            i.available = True
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')
        category = request.POST.get('category')
        if int(quantity) > 0:
            available = True
        elif int(quantity) <= 0:
            available = False
        Product.objects.create(name=name, price=price, quantity=quantity, available=available, category_id=category)
        return redirect('product')
    return render(request, 'product/product.html', context)


@login_required(login_url='login')
def category_view(request):
    context = {
        'category': Category.objects.all()
    }
    if request.method == 'POST':
        name = request.POST.get('name')
        Category.objects.create(name=name)
        return redirect('category')
    return render(request, 'product/category.html', context)


@login_required(login_url='login')
def food_view(request):
    context = {
        'category': Category.objects.all(),
        'food': Food.objects.all()
    }
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        category = request.POST.get('category')
        available = request.POST.get('available')
        if available is None:
            available = False
        Food.objects.create(
            name=name, price=price, category_id=category, available=available)
        return redirect('food')
    return render(request, 'product/food.html', context)


@login_required(login_url='login')
def room_view(request):
    context = {
        'room': Rooms.objects.all()
    }
    if request.method == 'POST':
        number = request.POST.get('number')
        place = request.POST.get('place')
        Rooms.objects.create(number=number, places=place)
        return redirect('room')
    return render(request, 'product/room.html', context)


@login_required(login_url='login')
def order_view(request):
    context = {
        'order': Order.objects.all(),
        'waiter': User.objects.filter(role=2),
        'room': Rooms.objects.all(),
    }
    if request.method == 'POST':
        user = request.POST.get('user')
        room = request.POST.get('room')
        owner = request.POST.get('owner')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        day = request.POST.get('date')
        delivery_date = request.POST.get('dd')
        delivery = request.POST.get('delivery')
        if delivery is None:
            delivery = False
            delivery_date = None
            address = None
        else:
            room = None
        Client.objects.create(name=owner, phone=phone)
        client = Client.objects.last()
        Order.objects.create(user_id=user, room_id=room, address=address, date=day,
                             delivery_date=delivery_date,
                             owner=client, delivery=delivery)
        return redirect('order')
    return render(request, 'product/order.html', context)


@login_required(login_url='login')
def order_item_view(request):
    day = date.today()
    context = {
        'order': Order.objects.filter(date__day=day.day),
        'item': OrderItem.objects.all()
    }
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
    return render(request, 'product/order-item.html', context)
