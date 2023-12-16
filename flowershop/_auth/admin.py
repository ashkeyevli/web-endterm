from django.contrib import admin

# Register your models here.
from _auth.models import  User, Manager, Admin, Customer, ManagerProfile, AdminProfile, CustomerProfile

admin.site.register(User)
admin.site.register(Manager)
admin.site.register(Admin)
admin.site.register(Customer)
admin.site.register(ManagerProfile)
admin.site.register(AdminProfile)
admin.site.register(CustomerProfile)