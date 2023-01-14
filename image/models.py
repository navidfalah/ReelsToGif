from django.db import models


class UrlVideo(models.Model):
    url = models.URLField()
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified = models.DateTimeField(auto_now=True, blank=True, null=True)
    
    def __str__(self):
        return self.url

