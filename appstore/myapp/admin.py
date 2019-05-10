from django.contrib import admin
from .models import *

admin.site.register(App)
admin.site.register(Bookmark)
admin.site.register(Download)
admin.site.register(Comment)
admin.site.register(Set_comment)

# Register your models here.
