# Generated by Django 3.1.6 on 2021-04-22 18:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя категории')),
                ('slug', models.SlugField(unique=True)),
                ('image', models.ImageField(default=None, upload_to='C:\\Users\\User\\Desktop\\flowerShop\\flowerShop\\flowershop\\product\\images\\category', verbose_name='Изображение')),
            ],
        ),
        migrations.CreateModel(
            name='Flower',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Наименование')),
                ('slug', models.SlugField(unique=True)),
                ('image', models.ImageField(default=None, upload_to='C:\\Users\\User\\Desktop\\flowerShop\\flowerShop\\flowershop\\product\\images\\flower', verbose_name='Изображение')),
                ('description', models.TextField(null=True, verbose_name='Описание')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Стоимость')),
                ('color', models.CharField(blank=True, default='Красная', max_length=255, null=True, verbose_name='Окраска цветка:')),
                ('stock', models.PositiveIntegerField(default=0, verbose_name='Скидка в процентах')),
                ('available', models.BooleanField(default=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.category', verbose_name='Категория')),
            ],
        ),
    ]