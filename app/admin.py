from django.contrib import admin
from  django.contrib.auth.admin import UserAdmin

# Register your models here.
from .models import *

class UserModel(UserAdmin):
    list_display = ["username",'user_type']

admin.site.register(CustomUser,UserModel)