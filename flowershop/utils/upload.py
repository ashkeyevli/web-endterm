import os
import shutil


def category_image_directory_path(instance, filename):
    return f'category_photos/{instance.name}/{filename}'

def product_image_directory_path(instance, filename):
    return f'flower_photos/{instance.title}/{filename}'

def event_image_directory_path(instance, filename):
    return f'events/{instance.title}/{filename}'


def manager_image_directory_path(instance, filename):
    return f'users/{instance.manager.role}/{instance.manager.username}/{filename}'

def admin_image_directory_path(instance, filename):
    return f'users/{instance.admin.role}/{instance.admin.username}/{filename}'

def admin_avatar_delete(filename):
    admin_avatar_path = os.path.abspath(os.path.join(filename.path, '../'))
    shutil.rmtree(admin_avatar_path)



def category_photo_delete(filename):
    category_photo_path = os.path.abspath(os.path.join(filename.path, '../'))

    shutil.rmtree(category_photo_path)

def flower_photo_delete(filename):
    flower_photo_path = os.path.abspath(os.path.join(filename.path, '../'))
    shutil.rmtree(flower_photo_path)

def event_photo_delete(filename):
    event_photo_path = os.path.abspath(os.path.join(filename.path, '../'))
    shutil.rmtree(event_photo_path)