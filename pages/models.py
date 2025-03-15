"""
Models for the pages app
"""
from django.db import models


class Page(models.Model):
    """
    Stores a single page whose content can be updated in the django admin
    """
    STATUS = ((0, "Draft"), (1, "Published"))

    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    content = models.TextField()
    page_title = models.CharField(max_length=64, null=True, blank=True)
    meta_description = models.CharField(max_length=254, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return str(self.title)
