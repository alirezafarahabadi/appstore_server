from django.db import models
from myuser.models import CustomUser
from django.conf import settings
from .validators import validate_file_extension, validate_file_size


class App(models.Model):

    APP_SUBJECTS = (
        ('action_game', 'action_game'),
        ('puzzle_game', 'puzzle_game'),
        ('driver_game', 'driver_game'),
        ('score_game', 'score_game'),
        ('sports_game', 'sports_game'),
        ('strategic_game', 'strategic_game'),
        ('weather_app', 'weather_app'),
        ('education_app', 'education_app'),
        ('tools_app', 'tools_app'),
        ('cooking_app', 'cooking_app'),
        ('lifestyle_app', 'lifestyle_app'),
        ('health_app', 'health_app'),
        ('social_app', 'social_app'),
        ('network_app', 'network_app'),
        ('media_app', 'media_app'),
    )

    name = models.CharField(max_length=30)
    app_description = models.CharField(max_length=200, blank=True)
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    subject = models.CharField(max_length=20, choices=APP_SUBJECTS)
    download_number = models.IntegerField(default=0)
    size = models.CharField(max_length=10)
    apk_file = models.FileField(upload_to='apk_files', validators=[validate_file_extension, validate_file_size])
    image = models.ImageField(upload_to='image_files')


class Download(models.Model):
    app = models.ForeignKey(App, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)


class Bookmark(models.Model):
    app = models.ForeignKey(App, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)


class Comment(models.Model):
    app = models.ForeignKey(App, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    comment = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now=True)

class Rate(models.Model):
    rate = models.CharField(max_length=4)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    app = models.ForeignKey(App, on_delete=models.CASCADE)
