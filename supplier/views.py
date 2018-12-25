from django.shortcuts import render
# from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Supplier


def home(request):
    context = {
        'posts': Supplier.objects.all()
    }
    return render(request, 'supplier/home.html', context)


class SupplierListView(ListView):
    model = Supplier
    template_name = 'supplier/home.html'       # <app>/<model>_<viewtype>.html
    context_object_name = 'suppliers'
    ordering = ['name_supplier']
    paginate_by = 5


class SupplierDetailView(DetailView):
    model = Supplier


class ItemCreateView(CreateView):
    model = Supplier
    fields = ['name_supplier']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ItemUpdateView(UpdateView):
    model = Supplier
    fields = ['name_supplier']


class ItemDeleteView(DeleteView):
    model = Supplier
    success_url = '/'


def about(request):
    return render(request, 'supplier/about.html', {'title': 'About'})

