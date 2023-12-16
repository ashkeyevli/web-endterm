from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin, AbstractUser
from django.db import models

from utils.upload import product_image_directory_path, admin_image_directory_path, manager_image_directory_path
from utils.validators import validate_size, validate_extension
from .constants import CUSTOMER_ROLE_ORDINARY, USER_ROLE_CUSTOMER, CUSTOMER_ROLES, USER_ROLES, USER_ROLE_ADMIN, USER_ROLE_MANAGER

class MainUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, password, **extra_fiels):
        if not username:
            raise ValueError('set username')
        user = self.model(username= username, **extra_fiels)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, password = None, **extra_fiels):
        extra_fiels.setdefault('is_superuser', True)
        return self._create_user(username, password, **extra_fiels)

    def create_superuser(self, username, password=None, **extra_fiels):
        extra_fiels.setdefault('is_superuser', True)
        if extra_fiels.get('is_superuser') is not True:
            raise ValueError('it is not superuser')
        return self._create_user(username, password, **extra_fiels)

class CustomerManager(MainUserManager):
    def get_related(self):
        return self.prefetch_related('related_orders')

class ManagerManager(MainUserManager):

    def get_related(self):
        return self.prefetch_related('events')

class AdminManager(MainUserManager):
    def create_superuser(self, username, password=None, **extra_fiels):
        extra_fiels.setdefault('is_superuser', True)
        if extra_fiels.get('is_superuser') is not True:
            raise ValueError('it is not superuser')
        return self._create_user(username, password, **extra_fiels)




class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField('username',max_length=30, unique=True)
    first_name = models.CharField(('first_name'),max_length=30, blank=True)
    last_name = models.CharField(('last_name'),max_length=30, blank=True)
    email = models.EmailField(('email'),max_length=30, blank=True)
    data_joined = models.DateTimeField('data_joined', auto_now_add=True)
    is_active = models.BooleanField('active', default=True)
    is_staff = models.BooleanField('staff', default=True)
    role = models.SmallIntegerField(choices=USER_ROLES, default=USER_ROLE_ADMIN)

    objects = MainUserManager()

    USERNAME_FIELD = 'username'


class Customer(User):
    customer_type = models.SmallIntegerField(choices=CUSTOMER_ROLES, default=CUSTOMER_ROLE_ORDINARY)
    location = models.CharField(max_length=30, blank=True)
    is_staff = False
    role = USER_ROLE_CUSTOMER
    objects = CustomerManager()


    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'

class CustomerProfile(models.Model):
    bio = models.TextField(max_length=500, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    customer = models.OneToOneField(Customer, on_delete = models.CASCADE)

    class Meta:
        verbose_name = 'Профиль Покупателя'
        verbose_name_plural = 'Профили Покупателей'


class Manager(User):

    salary = models.FloatField(null=True, blank=True , verbose_name="Salary")
    role = USER_ROLE_MANAGER
    objects = ManagerManager()
    class Meta:
        verbose_name = 'Manager'
        verbose_name_plural = 'Managers'

class ManagerProfile(models.Model):
    avatar = models.ImageField(upload_to= manager_image_directory_path, validators=[validate_size, validate_extension], null=True, blank=True, verbose_name='Изображение', default=r'users/profile.png')
    bio = models.TextField(max_length=500, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    manager = models.OneToOneField(Manager, on_delete = models.CASCADE)

    class Meta:
        verbose_name = 'Профиль Мэнеджера'
        verbose_name_plural = 'Профили Мэнеджеров'

class Admin(User):

    role = USER_ROLE_ADMIN
    objects = AdminManager()

    class Meta:
        verbose_name = 'Admin'
        verbose_name_plural = 'Admins'

class AdminProfile(models.Model):
    avatar = models.ImageField(upload_to= admin_image_directory_path, validators=[validate_size, validate_extension], null=True, blank=True, verbose_name='Изображение', default=r'media/users/profile.png')
    bio = models.TextField(max_length=500, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    admin = models.OneToOneField(Admin, on_delete = models.CASCADE)

    class Meta:
        verbose_name = 'Профиль Админов'
        verbose_name_plural = 'Профили Админов'