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


class Rooms(models.Model):
    number = models.IntegerField()
    places = models.IntegerField()


class Client(models.Model):
    name = models.CharField(max_length=1212)
    phone = models.BigIntegerField(null=True, blank=True)


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
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    available = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        quantity = int(self.quantity)
        if quantity <= 0:
            self.available = False
        else:
            self.available = True
        super(Product, self).save(*args, **kwargs)


class Order(models.Model):
    user = models.ForeignKey(User,  on_delete=models.CASCADE, null=True, blank=True)
    room = models.ForeignKey(Rooms, on_delete=models.CASCADE, null=True, blank=True)
    delivery = models.BooleanField(default=False)
    owner = models.CharField(max_length=210)
    address = models.CharField(max_length=210, null=True, blank=True)
    date = models.DateField()
    delivery_date = models.DateTimeField(null=True, blank=True)
    done = models.BooleanField(default=False)
    bill = models.IntegerField()


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField()
