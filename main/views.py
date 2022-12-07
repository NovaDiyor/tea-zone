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
        user = User.objects.filter(first_name=name)
        for i in user:
            print(i.first_name, name, password)
        if user.count() > 0:
            print(2)
            usr = authenticate(username=name, password=password)
            print(usr)
            if usr is not None:
                login(request, usr)
                return redirect('dashboard')
            else:
                return redirect('404')
        else:
            user = User.objects.filter(number=number)
            if user.count() > 0:
                print(1)
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
        return render(request, 'dashboard/dashboard-manager.html', context)
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
        order = Order.objects.all(done=True)
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
def waiters_view(request):
    user = request.user
    if user.role == 1:
        day = date.today()
        waiter = User.objects.filter(status=2)
        month = 0
        for i in waiter:
            order = Order.objects.filter(done=True, date__day=day.day, user=i)
            for x in order:
                item = OrderItem.objects.get(order=x)
                for n in item:
                    if n.product:
                        i.salary += n.quantity * n.product.price % 8
                    else:
                        i.salary += n.quantity * n.food.price % 8
                    month += i.salary
                    if i.date__day > day.day:
                        i.salary = 0
                    i.save()
        context = {
            'month': month,
            'waiters': waiter,
        }
        return render(request, 'staff/waiter.html', context)
    elif user.role == 3:
        day = date.today()
        waiter = User.objects.filter(status=2)
        month = 0
        for i in waiter:
            order = Order.objects.filter(done=True, date__day=day.day, user=i)
            for x in order:
                item = OrderItem.objects.get(order=x)
                for n in item:
                    if n.product:
                        i.salary += n.quantity * n.product.price % 8
                    else:
                        i.salary += n.quantity * n.food.price % 8
                    month += i.salary
                    if i.date__day > day.day:
                        i.salary = 0
                    i.save()
        context = {
            'month': month,
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
def product_view(request):
    usr = request.user
    if usr.role == 1:
        pro = Product.objects.all()
        for i in pro:
            if i.quantity <= 0:
                i.available = False
            else:
                i.available = True
        return render(request, 'product/product.html', pro)
    elif usr.role == 3:
        pro = Product.objects.all()
        for i in pro:
            if i.quantity <= 0:
                i.available = False
            else:
                i.available = True
        return render(request, 'product/product.html', pro)
    else:
        return redirect('404')
