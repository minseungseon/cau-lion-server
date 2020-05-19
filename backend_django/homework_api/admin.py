from django.contrib import admin
from django.db import models
from .models import Post, Files, Album
# Register your models here.

admin.site.register(Post)
admin.site.register(Album)
admin.site.register(Files)