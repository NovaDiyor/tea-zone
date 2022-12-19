from datetime import date, datetime
from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def paginator_page(List, num, request):
    paginator = Paginator(List, num)
    page = request.GET.get('page')
    try:
        lt = paginator.page(page)
    except PageNotAnInteger:
        lt = paginator.page(1)
    except EmptyPage:
        lt = paginator.page(paginator.num_page)
    return lt


def login_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        user = User.objects.filter(username=name)
        if user.count() > 0:
            usr = authenticate(username=name, password=password)
            if usr is not None:
                login(request, usr)
                return redirect('dashboard')
            else:
                return redirect('404')
    return render(request, 'login.html')


@login_required(login_url='login')
def logout_view(request):
    logout(request)
    return redirect('login')


def error_view(request):
    return render(request, '404.html')


@login_required(login_url='login')
def add_staff(request):
    try:
        if request.method == 'POST':
            username = request.POST.get('username')
            name = request.POST.get('name')
            last_name = request.POST.get('last-name')
            password = request.POST.get('password')
            confirm_password = request.POST.get('cp')
            number = request.POST.get('number')
            status = request.POST.get('status')
            f = 0
            for i in User.objects.all():
                if i.username == username:
                    f += 1
                else:
                    f += 0
            if f == 1:
                print('user is exist')
            elif f == 0:
                if confirm_password == password:
                    User.objects.create_user(
                        username=username, first_name=name,
                        last_name=last_name, password=password,
                        number=number, role=status)
            return redirect('staff')
        else:
            return render(request, 'staff/add-staff.html')
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
        if order.count() > 0:
            print(order.count())
            for i in order:
                item = OrderItem.objects.get(order=i)
                if item.count() > 0:
                    total += item.quantity * item.price % 8
                else:
                    pass
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
        context = {
            'client': client.count(),
            'staff': staff.count(),
            'total': order.count(),
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
            'call_canter': User.objects.filter(role=5),
            'objects': paginator_page(User.objects.filter(role=5), 5, request)
        }
        return render(request, 'staff/call-canter.html', context)
    elif usr.role == 3:
        context = {
            'call_center': User.objects.filter(role=5),
            'objects': paginator_page(User.objects.filter(role=5), 5, request)
        }
        return render(request, 'staff/call-canter.html', context)
    else:
        return redirect('404')


@login_required(login_url='login')
def client_view(request):
    context = {
        'client': Client.objects.all(),
        'objects': paginator_page(Client.objects.all(), 5, request),
    }
    return render(request, 'staff/client.html', context)


@login_required(login_url='login')
def product_view(request):
    pro = Product.objects.all()
    context = {
        'product': pro,
        'objects': paginator_page(Product.objects.all(), 5, request),
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
        'category': Category.objects.all(),
        'objects': paginator_page(Category.objects.all(), 5, request)
    }
    if request.method == 'POST':
        name = request.POST.get('name')
        Category.objects.create(name=name)
        return redirect('category')
    return render(request, 'product/category.html', context)


@login_required(login_url='login')
def staff_view(request):
    context = {
        'staff': paginator_page(User.objects.all(), 5, request),
        'total': User.objects.all().count()
    }
    return render(request, 'staff/staff.html', context)


@login_required(login_url='login')
def food_view(request):
    context = {
        'category': Category.objects.all(),
        'food': Food.objects.all(),
        'objects': paginator_page(Food.objects.all(), 5, request)
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
        'room': Rooms.objects.all(),
        'objects': paginator_page(Rooms.objects.all(), 5, request)
    }
    if request.method == 'POST':
        number = request.POST.get('number')
        place = request.POST.get('place')
        Rooms.objects.create(number=number, places=place)
        return redirect('room')
    return render(request, 'product/room.html', context)


@login_required(login_url='login')
def order_view(request):
    d = date.today()
    order = Order.objects.filter(delivery=False, done=False)
    for i in order:
        if i.date.day == d.day:
            r = Rooms.objects.get(id=i.room.id)
            r.busy = True
            r.save()
    try:
        if request.method == 'POST':
            day = datetime.strptime(request.POST.get('date'), "%m/%d/%Y").date()
            OrderDay.objects.create(day=day)
            return redirect('add-order')
        context = {
            'order': paginator_page(Order.objects.filter(delivery=False), 5, request),
            'food': Food.objects.filter(available=True),
            'product': Product.objects.filter(available=True)
        }
        return render(request, 'product/order.html', context)
    except Exception as err:
        return err


@login_required(login_url='login')
def add_order(request):
    room_list = []
    for i in Rooms.objects.all():
        room_list.append(i)
    for i in Order.objects.all():
        if i.date == OrderDay.objects.last().day:
            room_list.remove(i.room)
    try:
        if request.method == 'POST':
            user = request.POST.get('user')
            room = request.POST.get('room')
            client = request.POST.get('owner')
            phone = request.POST.get('phone')
            day = OrderDay.objects.last().day
            print(client, user, room, phone)
            print(day)
            f = 0
            for i in Client.objects.all():
                if i.phone == int(phone):
                    f += 1
                else:
                    f += 0
            print(f)
            if f == 1:
                cl = Client.objects.get(phone=phone)
                print(cl, day)
                Order.objects.create(user_id=user, room_id=room, owner=cl, delivery=False, date=day, bill=0)
                return redirect('order')
            elif f == 0:
                cl = Client.objects.create(name=client, phone=phone)
                print(cl)
                usr = User.objects.get(id=user)
                rm = Rooms.objects.get(id=room)
                print(usr, rm, day)
                Order.objects.create(user_id=user, room_id=room, owner=cl, delivery=False, date=day, bill=0)
                return redirect('order')
        context = {
            'room': room_list,
            'waiter': User.objects.filter(role=2),
        }
        return render(request, 'product/add-order.html', context)
    except Exception as err:
        print(err)


@login_required(login_url='login')
def delivery_view(request):
    d = datetime.today()
    order = Order.objects.filter(delivery_date__hour=d.hour)
    for i in order:
        i.done = True
        i.save()
    context = {
        'delivery': paginator_page(Order.objects.filter(delivery=True), 5, request),
    }
    try:
        if request.method == 'POST':
            owner = request.POST.get('owner')
            phone = request.POST.get('phone')
            day = datetime.strptime(request.POST.get('date'), "%m/%d/%Y").date()
            f = 0
            for i in Client.objects.filter(phone=phone):
                if i.count() > 0:
                    f += 1
                    cl = i
                else:
                    f += 0
            if f == 0:
                c = Client.objects.create(name=owner, phone=phone)
                Order.objects.create(delivery=True, date=day, bill=0, owner=c)
            else:
                Order.objects.create(delivery=True, date=day, bill=0, owner=cl)
    except Exception as err:
        print(err)


@login_required(login_url='login')
def order_item_view(request):
    day = date.today()
    context = {
        'order': Order.objects.filter(done=False),
        'item': paginator_page(OrderItem.objects.all(), 5, request),
        'product': Product.objects.filter(available=True),
        'food': Food.objects.filter(available=True),
    }
    if request.method == 'POST':
        order = request.POST.get('order')
        food = request.POST.get('food')
        product = request.POST.get('product')
        quantity = request.POST.get('quantity')
        if food == 'Nothing':
            pro = Product.objects.get(id=product)
            if int(quantity) > pro.quantity:
                quantity = pro.quantity
            pro.quantity -= int(quantity)
            pro.save()
            rd = Order.objects.get(id=order)
            rd.bill += pro.price * int(quantity)
            rd.save()
            OrderItem.objects.create(
                order=rd,
                product=pro,
                quantity=quantity)
        elif product == 'Nothing':
            fd = Food.objects.get(id=food)
            rd = Order.objects.get(id=order)
            rd.bill += fd.price * int(quantity)
            rd.save()
            OrderItem.objects.create(
                order=rd,
                food=fd,
                quantity=quantity)
        return redirect('order-item')
    return render(request, 'product/order-item.html', context)


@login_required(login_url='login')
def add_order_item(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        food = request.POST.get('food')
        product = request.POST.get('product')
        quantity = request.POST.get('quantity')
        if food == 'Nothing':
            pro = Product.objects.get(id=product)
            if int(quantity) > pro.quantity:
                quantity = pro.quantity
            pro.quantity -= int(quantity)
            pro.save()
            order.bill += pro.price * int(quantity)
            order.save()
            OrderItem.objects.create(
                order=order,
                product=pro,
                quantity=quantity)
        elif product == 'Nothing':
            fd = Food.objects.get(id=food)
            order.bill += fd.price * int(quantity)
            order.save()
            OrderItem.objects.create(
                order=order,
                food=fd,
                quantity=quantity)
        return redirect('order-item')
    context = {
        'food': Food.objects.all(),
        'product': Product.objects.all(),
    }
    return render(request, 'product/order.html', context)


@login_required(login_url='login')
def order_item_cooker(request):
    item = OrderItem.objects.all()
    order = []
    for i in item:
        if i.order.done == False:
            order.append(i)
    context = {
        'item': paginator_page(order, 5, request),
    }
    return render(request, 'product/cooker-item.html', context)

