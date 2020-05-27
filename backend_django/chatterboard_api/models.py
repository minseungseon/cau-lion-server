from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length = 200)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name = "custom_user_name", default = 1, on_delete = models.CASCADE)
    content = models.TextField()
    image = models.ImageField(upload_to="image")
    filename = models.FileField(blank=False, null=False, upload_to="files")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.title


