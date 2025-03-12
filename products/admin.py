"""
Configure the Django admin for the Product & Category models
"""
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Product, Category


@admin.register(Product)
class ProductAdmin(SummernoteModelAdmin):
    """
    Lists fields to display in admin, fields for search,
    filters, fields to prepopulate and rich-text editor.
    """
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'image',
    )
    ordering = ('sku',)
    search_fields = ['title', 'description']
    list_filter = ('status',)
    summernote_fields = ('description',)


class CategoryAdmin(admin.ModelAdmin):
    """
    Lists fields to display in admin
    """
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Category, CategoryAdmin)
