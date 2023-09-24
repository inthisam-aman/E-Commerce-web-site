# Generated by Django 4.1.4 on 2023-01-02 17:41

from django.db import migrations, models
import django.db.models.deletion
import shop.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('image', models.ImageField(blank=True, null=True, upload_to=shop.models.getfilename)),
                ('discription', models.TextField(max_length=500)),
                ('status', models.BooleanField(default=False, help_text='0-Show,1-Hidden')),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('vendor', models.CharField(max_length=150)),
                ('product_image', models.ImageField(blank=True, null=True, upload_to=shop.models.getfilename)),
                ('quantity', models.IntegerField()),
                ('original_price', models.FloatField()),
                ('selling_price', models.FloatField()),
                ('discription', models.TextField(max_length=500)),
                ('status', models.BooleanField(default=False, help_text='0-Show,1-Hidden')),
                ('trending', models.BooleanField(default=False, help_text='0-default,1-Trending')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.category')),
            ],
        ),
    ]
