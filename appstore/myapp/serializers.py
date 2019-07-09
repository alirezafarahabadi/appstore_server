from rest_framework import serializers
from .models import *


class AppSerializer(serializers.ModelSerializer):
    class Meta:
        model = App
        fields = ('name', 'app_description', 'creator',
                  'subject', 'download_number', 'size', 'apk_file', 'image')


class GetBriefAppSerializer(serializers.ModelSerializer):
    class Meta:
        model = App
        fields = ('name', 'subject', 'image', 'id')


class SaveCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('comment', 'user', 'app', 'date')


class GetCommentSerializer(serializers.Serializer):
    user = serializers.CharField()
    comment = serializers.CharField()
    date = serializers.DateTimeField()


class DownloadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Download
        fields = ('app', 'user')


class BookmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookmark
        fields = ('app', 'user')

class GetBookmarkSerializer(serializers.Serializer):
    user = serializers.CharField()
    app = serializers.CharField()


class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = ('app', 'user', 'rate')
