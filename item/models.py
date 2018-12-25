from django.db import models
from django.utils import timezone
from django.urls import reverse

from category.models import Category


class Item(models.Model):
    brand_item = models.CharField(max_length=255)
    type_item = models.CharField(max_length=255)
    name_item = models.CharField(max_length=255)
    note = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Category')
    cdUPC = models.CharField(max_length=255)
    # modified = models.DateTimeField(default=timezone.now, verbose_name='Modified')
    # created = models.DateTimeField(auto_now_add=True, verbose_name='Created')
    is_active = models.BooleanField(default=True, verbose_name='Is Active?')

    def __str__(self):
        return self.name_item

    def get_absolute_url(self):
        return reverse('item-detail', kwargs={'pk': self.pk})

    class Meta:
        managed = False
        verbose_name_plural = 'items'
        ordering = ['name_item']
        db_table = 'items'
