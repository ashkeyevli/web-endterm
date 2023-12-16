from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from _auth.models import Customer, Manager, Admin, CustomerProfile, AdminProfile, ManagerProfile
from utils.upload import admin_avatar_delete


@receiver(post_save, sender=Customer)
def customer_created(sender, instance, created, **kwargs):
    if created:
        CustomerProfile.objects.create(customer=instance)

@receiver(post_save, sender=Manager)
def manager_created(sender, instance, created, **kwargs):
    if created:
        ManagerProfile.objects.create(manager=instance)

@receiver(post_save, sender=Admin)
def admin_created(sender, instance, created, **kwargs):
    if created:
        AdminProfile.objects.create(admin=instance)


@receiver(post_delete, sender = AdminProfile )
def delete_avatar_on_profile_delete(sender, instance, **kwargs):
    avatar = instance.avatar
    if avatar:
        admin_avatar_delete(avatar)

@receiver(post_delete, sender = ManagerProfile )
def delete_avatar_of_manager_on_profile_delete(sender, instance, **kwargs):
    avatar = instance.avatar
    if avatar:
        admin_avatar_delete(avatar)