from django.contrib import admin
from .models import *

admin.site.register(app)
admin.site.register(bookmark)
admin.site.register(download)
admin.site.register(comment)
admin.site.register(set_comment)

# Register your models here.
