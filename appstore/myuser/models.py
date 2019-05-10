from django.core.exceptions import ValidationError
from django.utils.translation import ngettext
from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class CustomUser(AbstractUser):
    mobile_number = models.CharField(max_length=11)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @classmethod
    def custom_user_create(cls, username, email, password, first_name, last_name, mobile_number):
        username = cls.normalize_username(username)
        user = cls.objects.create_user(
            username=username,
            password=password,
            email=email,
            first_name=first_name,
            last_name=last_name,
            mobile_number=mobile_number
        )
        return user
