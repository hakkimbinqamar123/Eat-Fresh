# Generated by Django 4.1.1 on 2022-11-06 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deliveryapp', '0008_staff_gender_staff_photo_staff_verification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='photo',
            field=models.ImageField(upload_to='images/', verbose_name='Your Photo'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='verification',
            field=models.ImageField(upload_to='images/', verbose_name='Adhar/Election/Driving/PAN ID'),
        ),
    ]
