# Generated by Django 4.1.1 on 2022-12-01 04:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deliveryapp', '0017_products_shop_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='product_name',
            new_name='productname',
        ),
        migrations.RenameField(
            model_name='products',
            old_name='quantity_available',
            new_name='quantity',
        ),
    ]