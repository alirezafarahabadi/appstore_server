from rest_framework import serializers
from .models import *


class AppSerializer(serializers.ModelSerializer):
    class Meta:
        model = App
        fields = ('name', 'app_description', 'creator',
                  'subject', 'download_number', 'size', 'apk_file', 'image')


class Get_brief_app_serializer(serializers.ModelSerializer):
    class Meta:
        model = App
        fields = ('name', 'subject', 'image', 'id')


class Comment_serializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('text', 'user', 'app')


class Download_rate_serializer(serializers.ModelSerializer):
    class Meta:
        model = Download
        fields = ('app', 'user')


class Bookmark_serializer(serializers.ModelSerializer):
    class Meta:
        model = Bookmark
        fields = ('app', 'user')


class Rate_serializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = ('app', 'user', 'rate')
