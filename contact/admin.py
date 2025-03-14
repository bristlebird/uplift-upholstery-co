"""
Configure the Django admin for the Conhtact Enquiry model
"""
from django.contrib import admin
from .models import Enquiry


class EnquiryAdmin(admin.ModelAdmin):
    """
    Lists contact enquiries in admin
    """
    list_display = (
        'name',
        'email',
        'created_on',
    )
    ordering = ('-created_on',)
    search_fields = ['name', 'email', 'message']


admin.site.register(Enquiry, EnquiryAdmin)
