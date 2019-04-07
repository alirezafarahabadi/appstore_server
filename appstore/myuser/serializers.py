from rest_framework import serializers
from .models import custom_user
from django.conf import settings
from django.contrib.auth import get_user_model



class customuser_serializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('username', 'first_name', 'last_name',
     
                  'email', 'password', 'mobile_number')
