from django.db import models
from django.utils import timezone
from django.urls import reverse


class Category(models.Model):

    name_category = models.CharField(max_length=255, verbose_name='Category Name')
    is_food = models.BooleanField(default=False, verbose_name='Is Food?')
    modified_by = models.IntegerField()
    # modified = models.DateTimeField(default=timezone.now, verbose_name='Modified')
    created_by = models.IntegerField()
    # created = models.DateTimeField(auto_now_add=True, verbose_name='Created')
    is_active = models.BooleanField(default=True, verbose_name='Is Active?')

    def __str__(self):
        return self.name_category

    def get_absolute_url(self):
        return reverse('category-detail', kwargs={'pk': self.pk})

    class Meta:
        managed = False
        verbose_name_plural = 'categories'
        ordering = ['name_category']
        db_table = 'categories'
