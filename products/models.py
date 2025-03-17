from django.db import models
from django.core.validators import MinValueValidator


class Category(models.Model):
    """
    Stores a single category, used to categorise products
    """
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return str(self.name)

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    """
    Stores a single product related to :model: `product.Category`
    """
    STATUS = ((0, "Draft"), (1, "Published"))
    PRODUCT_TYPES = (
        ("furniture", "Furniture"),
        ("course", "Courses"),
        ("event", "Events")
    )

    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    page_title = models.CharField(max_length=64, null=True, blank=True)
    meta_description = models.CharField(max_length=254, null=True, blank=True)
    type = models.CharField(
        max_length=64, choices=PRODUCT_TYPES, default="Furniture")
    track_quantity = models.BooleanField(default=0)
    quantity_available = models.IntegerField(
        default=0, validators=[MinValueValidator(0)])
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return str(self.name)
