# from django.contrib import admin
# # from .models import Imagen

# # admin.site.register(Imagen)

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'first_name', 'last_name', 'email', 'profile_picture']

# Register your models with the admin site
admin.site.register(CustomUser, CustomUserAdmin)
