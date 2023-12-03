from django.db import models
from django.core.validators import RegexValidator
from datetime import date



# Create your models here.


class User_details(models.Model):
    user_id = models.IntegerField("Id of user", primary_key=True)
    username = models.CharField("Name of user", max_length=50)
    email = models.EmailField("Email", unique=True, blank=False)
    phone = models.IntegerField("Phone number")
    password = models.CharField("Password", max_length=25)
    usertype = models.CharField("Usertype", max_length=25, default='u')


class Products(models.Model):
    product_id=models.IntegerField("Id of product", primary_key=True)
    productname=models.CharField("Name", max_length=50)
    quantity=models.IntegerField("Quantity")
    price=models.FloatField("price")
    photo = models.ImageField("product picture", upload_to='images/')
    shop_id = models.IntegerField('shop id')

class Staff(models.Model):
    staff_id=models.IntegerField("Id of staff", primary_key=True)
    username=models.CharField("Name", max_length=50)
    phoneno = models.IntegerField("Phone number")
    state = models.CharField("Name", max_length=25, default='kerala')
    district = models.CharField("Name", max_length=50)
    address = models.CharField("Name", max_length=250)
    email = models.EmailField("Email")
    password = models.CharField("Password", max_length=25, default="a")
    shop_id = models.IntegerField('shop id', default=1)
    usertype = models.CharField("Usertype", max_length=25, default='w')
    photo = models.ImageField("Your Photo", upload_to='images/', default=0)
    gender = models.CharField("Gender", max_length=1, default='M')
    verification = models.ImageField("Adhar/Election/Driving/PAN ID", upload_to='images/', default=0)



class Cart(models.Model):
    cart_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User_details, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE)
    no_of_items = models.IntegerField("No of items")
    total_price = models.FloatField("Total price")


class Order_details(models.Model):
    order_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User_details, on_delete=models.CASCADE)
    total_price = models.FloatField("Total price")
    date = models.DateField("Date of order", default=date.today)


class Purchase(models.Model):
    card = models.CharField(max_length=25)
    qty = models.IntegerField("qty")
    number = models.CharField(max_length=25)
    cvv = models.CharField(max_length=25)



