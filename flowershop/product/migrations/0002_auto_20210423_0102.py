# Generated by Django 3.1.6 on 2021-04-22 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(default=None, upload_to='C:\\Users\\User\\Desktop\\flowerShop\\flowerShop\\flowershop\\media', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='flower',
            name='image',
            field=models.ImageField(default=None, upload_to='C:\\Users\\User\\Desktop\\flowerShop\\flowerShop\\flowershop\\product\\media', verbose_name='Изображение'),
        ),
    ]
