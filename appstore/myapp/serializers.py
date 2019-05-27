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
        fields = ('text', 'date')


class Download_rate_serializer(serializers.ModelSerializer):
    class Meta:
        model = Download
        fields = ('app', 'user', 'date')


class Bookmark_serializer(serializers.ModelSerializer):
    class Meta:
        model = Bookmark
        fields = ('app', 'user')


class Set_comment_serializer(serializers.ModelSerializer):
    class Meta:
        model = Set_comment
        fields = ('app', 'user', 'comment')
