from django.shortcuts import render, render_to_response
from django.db.models import F, Max, Sum
from django.views.generic import View
from list.models import List
from item.models import Item


def slist(request, list_id=1):
    return render_to_response('list/list.html',
                              {'list': List.objects.get(id=list_id)})


def lists(request):
    table = ListTable(List.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'list/lists.html', {'table': table})


class LatestListView(View):

    template_name = 'list/latest-list.html'

    model = List

    ldate = List.objects.annotate(max_date=Max('date_purchased')).filter(date_purchased=F('max_date'))[0]
#     tcost = List.objects.aggregate(total_cost_total=Sum('cost_total'))
#     print(tcost)
    table = ListTable(List.objects.filter(date_purchased__gte=ldate.date_purchased)
                                  .filter(supplier_id__exact=ldate.supplier_id))
    #                               .filter(item_id__exact=ldate.item_id))
    #                               .aggregate(total_cost_total=Sum('cost_total')))
    #    total_cost_total = sum(ldate.cost_total)
    # print(ldate.total_cost_total)

#    def total_cost(self):
#        return self.objects.aggregate(total_cost_total=Sum('cost_total'))

    def get(self, request):

        RequestConfig(request).configure(self.table)
        return render(request, self.template_name, {'table': self.table})