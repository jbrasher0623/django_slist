from django.db import models


class Supplier(models.Model):

    name_supplier = models.CharField(max_length=255, verbose_name='Supplier Name')

    def __str__(self):
        return self.name_supplier

    class Meta:
        managed = False
        verbose_name_plural = 'suppliers'
        ordering = ['name_supplier']
        db_table = 'suppliers'
