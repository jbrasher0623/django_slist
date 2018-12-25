from django.contrib import admin
# from item.models import Item
from list.models import List


class ListAdmin(admin.ModelAdmin):
    list_display = ('date_purchased', 'supplier', 'count_weight', 'cost_per_item', 'total_cost_items',
                    'amt_discount', 'perc_rate_sales_tax', 'amt_sales_tax', 'cost_total',)
    search_fields = ('date_purchased',)
    list_filter = ('date_purchased',)
#     date_hierarchy = 'modified'
    ordering = ['-date_purchased', 'supplier']


admin.site.register(List, ListAdmin)
