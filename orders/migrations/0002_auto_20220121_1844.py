# Generated by Django 3.1 on 2022-01-21 18:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderproduct',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='orderproduct',
            name='quantityingrams',
        ),
    ]
