# Generated by Django 4.1.1 on 2022-12-07 06:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deliveryapp', '0021_purchase'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchase',
            name='tm',
        ),
    ]
