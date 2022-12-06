from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import authenticate, login


def login_view(request):
    user = request.user
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


def waiters_view(request):
    user = request.user
    if user.role == 1:
        waiters = User.objects.filter(role=2)
    elif user.role == 3:
        waiters = User.objects.filter(role=2)
    context = {
        'waiters': waiters
    }
    return render(request, 'waiter.html', context)


