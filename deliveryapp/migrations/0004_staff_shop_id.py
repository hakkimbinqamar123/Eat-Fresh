# Generated by Django 4.1.1 on 2022-11-06 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deliveryapp', '0003_alter_staff_address_alter_staff_district_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='shop_id',
            field=models.IntegerField(default=1, verbose_name='shop id'),
        ),
    ]
