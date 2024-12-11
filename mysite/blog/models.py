from django.db import models
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    body = models.TextField()
    publish = models.DataTimeField(default=timezone.now)
    created = models.DataTimeField(auto_now_and=True)
    updated = models.DataTimeField(auto_now=True)

    def __str__(self):
        return self.title
    