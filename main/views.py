from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


def login_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        user = User.objects.filter(name=name)
        if user.count > 0:
            usr = authenticate(name=name, password=password)
            if usr is not None:
                login(request, usr)
                if usr.role == 1:
                    return redirect('dashboard')
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
            else:
                return redirect('login')
        else:
            return redirect('login')
    else:
        return render(request, 'login.html')


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
    elif usr.role == 3:
        pro = Product.objects.all()
        for i in pro:
            if i.quantity <= 0:
                i.available = False
            else:
                i.available = True
        return render(request, 'product.html', pro)
    else:
        return redirect('404')


@login_required(login_url='login')
def waiters_view(request):
    user = request.user
    if user.role == 1:
        waiters = User.objects.filter(role=2)
    elif user.role == 3:
        waiters = User.objects.filter(role=2)
    else:
        return redirect('404')
    context = {
        'waiters': waiters
    }
    return render(request, 'waiter.html', context)


def error_view(request):
    return render(request, '404.html')
