# Generated by Django 4.1.4 on 2023-02-27 16:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_favourite'),
    ]

    operations = [
        migrations.RenameField(
            model_name='favourite',
            old_name='product',
            new_name='product_qty',
        ),
    ]