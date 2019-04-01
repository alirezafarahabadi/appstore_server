from django.db import models
from myuser.models import user


class app(models.Model):
    name = models.CharField(max_length=30)
    app_description = models.CharField(max_length=200, blank=True)
    creator = models.CharField(max_length=20)
    subject = models.CharField(max_length=20)
    download_number = models.IntegerField(default=0)
    size = models.CharField(max_length=10)

class comment(models.Model):
    text = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now=True)

class download(models.Model):
    app=models.ForeignKey(app,on_delete = models.DO_NOTHING)
    user=models.ForeignKey(user,on_delete = models.CASCADE)
    date = models.DateTimeField(auto_now=True)

class bookmark(models.Model):   
    app=models.ForeignKey(app,on_delete = models.CASCADE)
    user=models.ForeignKey(user,on_delete = models.CASCADE)

class set_comment(models.Model):
    app=models.ForeignKey(app,on_delete = models.DO_NOTHING)
    user=models.ForeignKey(user,on_delete = models.DO_NOTHING)
    comment=models.ForeignKey(comment,on_delete = models.DO_NOTHING)
