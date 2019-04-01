from django.db import models

# Create your models here.

class user(models.Model):
    email = models.CharField(max_length=30)
    mobile_number = models.CharField(max_length=11)
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=30)
    user_name = models.CharField(primary_key=True, max_length=20)
