# Generated by Django 4.0.6 on 2022-07-08 06:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_soldproduct'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SoldProduct',
            new_name='ProductBill',
        ),
    ]
