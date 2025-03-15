"""
Models for Contact form app to allow enquiries to be saved
& reviewed by Store Owner
"""
from django.db import models


class Enquiry(models.Model):
    """
    Stores a single contact enquiry in Django admin
    """
    name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    message = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_on"]
        verbose_name_plural = 'Enquiries'

    def __str__(self):
        return f"Message from {self.name} — {self.email}"
