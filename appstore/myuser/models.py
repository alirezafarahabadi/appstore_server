from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class custom_user(AbstractUser):
    mobile_number = models.CharField(max_length=11)

    def __init__(self):
        super().__init__()
