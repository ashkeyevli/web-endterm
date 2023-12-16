from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from _auth.models import Customer, Manager, Admin, CustomerProfile, AdminProfile, ManagerProfile
from events.models import Event
from product.models import Category, Flower
from utils.upload import admin_avatar_delete, category_photo_delete, flower_photo_delete, event_photo_delete


@receiver(post_delete, sender = Event )
def delete_photo_on_event_delete(sender, instance, **kwargs):
    photo = instance.image
    if photo:
        event_photo_delete(photo)

