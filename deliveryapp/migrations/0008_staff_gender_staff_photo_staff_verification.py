# Generated by Django 4.1.1 on 2022-11-06 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deliveryapp', '0007_alter_user_details_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='gender',
            field=models.CharField(default='M', max_length=1, verbose_name='Gender'),
        ),
        migrations.AddField(
            model_name='staff',
            name='photo',
            field=models.ImageField(default=0, upload_to='images/', verbose_name='Your Photo'),
        ),
        migrations.AddField(
            model_name='staff',
            name='verification',
            field=models.ImageField(default=0, upload_to='images/', verbose_name='Adhar/Election/Driving/PAN ID'),
        ),
    ]
