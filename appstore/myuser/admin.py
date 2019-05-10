from django.contrib import admin
from django.contrib.auth import get_user_model

class UserAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        if request.user.is_superuser:
            obj.is_staff = True
            obj.save()


admin.site.register(get_user_model(), UserAdmin)


# Register your models here.
