# Generated by Django 3.1.6 on 2021-04-22 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_auto_20210423_0110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(default=None, upload_to='..product/images/category', verbose_name='Изображение'),
        ),
    ]
