# Generated by Django 3.1 on 2022-06-28 14:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0003_auto_20220112_0133'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartitem',
            old_name='quantity',
            new_name='color',
        ),
    ]
