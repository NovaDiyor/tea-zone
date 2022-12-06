from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


def login_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        number = request.POST.get('number')
        if number is None:
            number = 1
        print(name, password, number)
        user = User.objects.filter(first_name=name)
        if user.count() > 0:
            print(2)
            usr = authenticate(first_name=name, password=password)
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
            else:
                user = User.objects.filter(username=name)
                if user.count() > 0:
                    print(3)
                    usr = authenticate(username=name, password=password)
                    if usr:
                        login(request, usr)
                        return redirect('dashboard')
                    else:
                        return redirect('404')
            return redirect('login')
    return render(request, 'login.html')


def error_view(request):
    return render(request, '404.html')


@login_required(login_url='login')
def dashboard_waiter(request):
    usr = request.user
    if usr.role == 2:
        return render(request, 'dashboard/dashboard-waiter.html')
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
        return render(request, 'dashboard/dashboard.html')
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
        waiters = User.objects.filter(role=2)
        context = {
            'waiters': waiters
        }
        return render(request, 'staff/waiter.html', context)
    elif user.role == 3:
        waiters = User.objects.filter(role=2)
        context = {
            'waiters': waiters
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
