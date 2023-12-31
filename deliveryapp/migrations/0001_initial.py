# Generated by Django 4.1.2 on 2022-10-27 14:20

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('product_id', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id of product')),
                ('product_name', models.CharField(max_length=50, verbose_name='Name')),
                ('quantity_available', models.IntegerField(verbose_name='Quantity')),
                ('price', models.FloatField(verbose_name='price')),
                ('photo', models.ImageField(upload_to='images/', verbose_name='product picture')),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('staff_id', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id of staff')),
                ('username', models.CharField(max_length=50, verbose_name='Name')),
                ('ph_no', models.IntegerField(verbose_name='Phone number')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('password', models.CharField(default='a', max_length=25, verbose_name='Password')),
                ('usertype', models.CharField(default='s', max_length=25, verbose_name='Usertype')),
            ],
        ),
        migrations.CreateModel(
            name='User_details',
            fields=[
                ('user_id', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id of user')),
                ('username', models.CharField(max_length=50, verbose_name='Name of user')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('phone', models.IntegerField(verbose_name='Phone number')),
                ('password', models.CharField(default='a', max_length=25, verbose_name='Password')),
                ('usertype', models.CharField(default='u', max_length=25, verbose_name='Usertype')),
            ],
        ),
        migrations.CreateModel(
            name='Shops',
            fields=[
                ('shop_id', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id of shop')),
                ('shop_name', models.CharField(max_length=100, verbose_name='Name of shop')),
                ('ph_no', models.IntegerField(verbose_name='Phone number')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('address', models.CharField(max_length=250, verbose_name='Address of the shop')),
                ('staff_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='deliveryapp.staff')),
            ],
        ),
        migrations.CreateModel(
            name='Order_details',
            fields=[
                ('order_id', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id of order')),
                ('total_price', models.FloatField(verbose_name='Total price')),
                ('date', models.DateField(default=datetime.date.today, verbose_name='Date of order')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='deliveryapp.user_details')),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('cart_id', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id of cart')),
                ('no_of_items', models.IntegerField(verbose_name='No of items')),
                ('total_price', models.FloatField(verbose_name='Total price')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='deliveryapp.products')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='deliveryapp.user_details')),
            ],
        ),
    ]
