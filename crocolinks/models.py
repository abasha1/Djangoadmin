from django.db import models

class CrocoLink(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    link =  models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} -> {}".format(self.title, self.link)