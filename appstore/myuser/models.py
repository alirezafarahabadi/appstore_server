from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class custom_user(AbstractUser):
    mobile_number = models.CharField(max_length=11)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @classmethod
    def create_user(cls,username, email, password, first_name, last_name, mobile_number):
        """
        Create and save a user with the given username, email, and password.
        """
        if not username:
            raise ValueError('The given username must be set')
        username = cls.normalize_username(username)
        # if cls.objects.filter(username=username).exists():
        #     raise FileExistsError("username is taken")
        user = cls.objects.create_user(
            username=username,
            password=password,
            email=email,
            first_name=first_name,
            last_name=last_name,
            mobile_number=mobile_number
        )
        return user
