# Generated by Django 4.1.1 on 2022-11-06 06:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deliveryapp', '0005_staff_usertype'),
    ]

    operations = [
        migrations.RenameField(
            model_name='staff',
            old_name='staffname',
            new_name='username',
        ),
    ]