# Generated by Django 4.1.1 on 2022-11-06 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deliveryapp', '0004_staff_shop_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='usertype',
            field=models.CharField(default='w', max_length=25, verbose_name='Usertype'),
        ),
    ]
