from django.db import models
from django.urls import reverse
# Create your models here.
from utils.upload import category_image_directory_path, product_image_directory_path
from utils.validators import validate_size, validate_extension


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя категории')
    image = models.ImageField(upload_to= category_image_directory_path, validators=[validate_size, validate_extension], null=True, blank=True, verbose_name='Изображение')


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'slug': self.slug})


class Flower(models.Model):
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE, related_name='flowers')
    title = models.CharField(max_length=255, verbose_name='Наименование')
    image = models.ImageField(upload_to= product_image_directory_path, validators=[validate_size, validate_extension], null=True, blank=True, verbose_name='Изображение')
    description = models.TextField(verbose_name='Описание', null=True)
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Стоимость')
    color = models.CharField(max_length=255, verbose_name='Окраска цветка:', default='Красная', null=True, blank=True)
    stock = models.PositiveIntegerField('Скидка в процентах', default=0)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'slug': self.slug})