# Generated by Django 4.1.1 on 2022-12-07 06:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deliveryapp', '0026_remove_purchase_product_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchase',
            name='dt',
        ),
    ]
