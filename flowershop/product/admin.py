from django.contrib import admin

# Register your models here.
from product.models import  Flower, Category

admin.site.register(Flower)
admin.site.register(Category)
