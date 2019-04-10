from django.db import models
from myuser.models import custom_user
from django.conf import settings


class app(models.Model):
    name = models.CharField(max_length=30)
    app_description = models.CharField(max_length=200, blank=True)
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    subject = models.CharField(max_length=20)
    download_number = models.IntegerField(default=0)
    size = models.CharField(max_length=10)
    apk_file = models.FileField(upload_to='apk_files')
    image = models.ImageField(upload_to='image_files')


class comment(models.Model):
    text = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now=True)


class download(models.Model):
    app = models.ForeignKey(app, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)


class bookmark(models.Model):
    app = models.ForeignKey(app, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)


class set_comment(models.Model):
    app = models.ForeignKey(app, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    comment = models.ForeignKey(comment, on_delete=models.DO_NOTHING)
