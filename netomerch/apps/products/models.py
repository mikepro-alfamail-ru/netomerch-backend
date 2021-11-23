import django.db.models.enums
from django.db import models
from django.db.models import JSONField
from django.utils.translation import gettext_lazy as _
from taggit.managers import TaggableManager

# up-level Category


class Category(models.Model):
    class Meta:
        verbose_name_plural = _("Categories")

    name = models.CharField(max_length=50, null=False, default='')
    short_description = models.CharField(max_length=50, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to='categories')

    def __str__(self):
        return f"{self.id}: name {self.name}"


class ItemProperty(models.Model):
    class PropertyType(django.db.models.enums.Choices):
        TEXT = 'TEXT'
        NUMBER = 'NUMB'
        BOOLEAN = 'BOOL'

    class Meta:
        verbose_name = "Item property"
        verbose_name_plural = "Item Properties"

    name = models.CharField(max_length=50)
    type = models.CharField(max_length=4, choices=PropertyType.choices, blank=False,
                            null=False, default=PropertyType.TEXT, verbose_name=_('type'))
    description = models.TextField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.id}: property {self.name} ({self.type})"


class Item(models.Model):
    class Meta:
        verbose_name_plural = _("Items")

    category = models.ManyToManyField(Category)
    price = models.DecimalField(max_digits=13, decimal_places=2, default=0.00, blank=False, null=False)
    name = models.CharField(max_length=50, default='', blank=False, null=False)
    short_description = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='item', blank=True, null=True)
    is_published = models.BooleanField(default=False, blank=False, null=False)
    tags = TaggableManager(blank=True)
    properties = JSONField(default=dict)

    def __str__(self):
        return f"{self.id}: name {self.name}"
