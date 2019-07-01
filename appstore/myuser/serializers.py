from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password


class CustomuserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('username', 'first_name', 'last_name',

                  'email', 'mobile_number', 'id')


class SaveCustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('username', 'first_name', 'last_name',

                  'email', 'mobile_number', 'password')
        write_only_fields = ('password',)
        read_only_fields = ('id',)
