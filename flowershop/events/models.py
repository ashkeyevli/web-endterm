from django.db import models

# Create your models here.
from _auth.models import Manager
from utils.upload import event_image_directory_path
from utils.validators import validate_size, validate_extension


class Event(models.Model):
    manager = models.ForeignKey(Manager, verbose_name='Автор', on_delete=models.CASCADE, related_name='events')
    title = models.CharField(max_length=255, verbose_name='Наименование')
    image = models.ImageField(upload_to= event_image_directory_path, validators=[validate_size, validate_extension], null=True, blank=True, verbose_name='Изображение')
    description = models.TextField(verbose_name='Описание', null=True)

    class Meta:
        verbose_name = 'Event'
        verbose_name_plural = 'Events'

    def __str__(self):
        return self.title