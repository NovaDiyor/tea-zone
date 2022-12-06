from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    role = models.SmallIntegerField(choices=(
        (1, 'director'),
        (2, 'waiter'),
        (3, 'manager'),
        (4, 'cooker'),
        (5, 'call-center'),
    ), null=True, blank=True)
    number = models.BigIntegerField(null=True, blank=True)
    img = models.ImageField(upload_to='users/', null=True, blank=True)
    salary = models.IntegerField(default=0, null=True, blank=True)
    is_waiter = models.BooleanField()
    
    def save(self, *args, **kwargs):
        if self.role == 2:
            self.is_waiter = True
        else:
            self.is_waiter = False
        super(User, self).save(*args, **kwargs)


class Rooms(models.Model):
    number = models.IntegerField()
    places = models.IntegerField()


class Client(models.Model):
    name = models.CharField(max_length=1212)
    phone = models.BigIntegerField()


class Category(models.Model):
    name = models.CharField(max_length=210)


class Food(models.Model):
    name = models.CharField(max_length=23232)
    price = models.DecimalField(max_digits=50, decimal_places=2)
    available = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)


class Product(models.Model):
    name = models.CharField(max_length=210)
    price = models.IntegerField()
    quantity = models.IntegerField()
    available = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        quantity = int(self.quantity)
        if quantity <= 0:
            self.available = False
        else:
            self.available = True
        super(Product, self).save(*args, **kwargs)


class Order(models.Model):
    user = models.ForeignKey(User,  on_delete=models.CASCADE, null=True,blank=True)
    room = models.ForeignKey(Rooms, on_delete=models.CASCADE, null=True, blank=True)
    delivery = models.BooleanField(default=False)
    owner = models.ForeignKey(Client, on_delete=models.CASCADE)
    address = models.CharField(max_length=23232)
    date = models.DateField()
    delivery_date = models.DateTimeField()
    done = models.BooleanField(default=False)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    quantity = models.IntegerField()
