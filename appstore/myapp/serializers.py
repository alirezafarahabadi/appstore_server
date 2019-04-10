from rest_framework import serializers
from .models import *


class get_app_serializer(serializers.ModelSerializer):
    class Meta:
        model = app
        # fields = ('name', 'app_description', 'creator',
        #           'subject', 'download_number', 'size', 'apk_file')
        exclude = ('apk_file', 'image')


class save_app_serializer(serializers.ModelSerializer):
    class Meta:
        model = app
        fields = ('name', 'app_description', 'creator',
                  "subject", 'download_number', 'size', 'apk_file')


class comment_serializer(serializers.ModelSerializer):
    class Meta:
        model = comment
        fields = ('text', 'date')


class download_rate_serializer(serializers.ModelSerializer):
    class Meta:
        model = download
        fields = ('app', 'user', 'date')


class bookmark_serializer(serializers.ModelSerializer):
    class Meta:
        model = bookmark
        fields = ('app', 'user')


class set_comment_serializer(serializers.ModelSerializer):
    class Meta:
        model = set_comment
        fields = ('app', 'user', 'comment')
