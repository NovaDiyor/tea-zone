
from django.shortcuts import render, redirect
from .models import *


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
                    if status == 2:
                        User.objects.create_user(
                            first_name=name, last_name=last_name,
                            password=password, number=number,
                            status=status)
                        return redirect('staff')
                    elif status == 3:
                        User.objects.create_user(
                            first_name=name, last_name=last_name,
                            password=password,number=number,
                            status=status)
                        return redirect('staff')
                    elif status == 4:
                        User.objects.create_user(
                            first_name=name, last_name=last_name,
                            password=password, number=number,
                            status=status)
                        return redirect('staff')
                    elif status == 5:
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
                    if status == 2:
                        User.objects.create_user(
                            first_name=name, last_name=last_name,
                            password=password, number=number,
                            status=status)
                        return redirect('staff')
                    elif status == 3:
                        User.objects.create_user(
                            first_name=name, last_name=last_name,
                            password=password,number=number,
                            status=status)
                        return redirect('staff')
                    elif status == 4:
                        User.objects.create_user(
                            first_name=name, last_name=last_name,
                            password=password, number=number,
                            status=status)
                        return redirect('staff')
                    elif status == 5:
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
