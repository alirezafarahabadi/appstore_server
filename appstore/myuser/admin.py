from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin

admin.site.register(custom_user, UserAdmin)


# Register your models here.
