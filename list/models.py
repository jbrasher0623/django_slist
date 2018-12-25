from django.db import models
from item.models import Item
from supplier.models import Supplier


class List(models.Model):

    item = models.ForeignKey(Item, blank=False, null=False, on_delete=models.CASCADE, verbose_name='Item Name')

    date_purchased = models.DateField(blank=False, null=False, verbose_name='Date Purchased')

    supplier = models.ForeignKey(Supplier, blank=False, null=False, on_delete=models.CASCADE,
                                 verbose_name='Supplier Name')

    count_weight = models.DecimalField(max_digits=3, decimal_places=0, default=0, verbose_name='Count_Weight')
    cost_per_item = models.DecimalField(max_digits=11, decimal_places=4, default=0.0000, verbose_name='Cost per Item')
    total_cost_items = models.DecimalField(max_digits=11, decimal_places=4, default=0.0000,
                                           verbose_name='Total Cost of Items')
    amt_discount = models.DecimalField(max_digits=11, decimal_places=4, default=0.0000, verbose_name='Discount Amount')
    perc_rate_sales_tax = models.DecimalField(max_digits=4, decimal_places=2,
                                              default=0.00, verbose_name='Sales Tax Rate %')
    amt_sales_tax = models.DecimalField(max_digits=11, decimal_places=4,
                                        default=0.0000, verbose_name='Sales Tax Amount')
    cost_total = models.DecimalField(max_digits=11, decimal_places=4, default=0.0000, verbose_name='Total Cost')

    def __str__(self):
        return str(self.date_purchased)

    class Meta:
        managed = False
        verbose_name_plural = 'lists'
        ordering = ['-date_purchased', 'supplier', 'item']
        db_table = 'lists'
