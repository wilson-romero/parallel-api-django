import uuid

from django.db import models
from django.utils.text import slugify
from markdownx.models import MarkdownxField


class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code = models.CharField(max_length=50, unique=True, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    name = models.CharField(max_length=255)
    description = MarkdownxField()
    is_published = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


