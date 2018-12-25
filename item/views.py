from django.shortcuts import render
# from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Item


def home(request):
    context = {
        'posts': Item.objects.all()
    }
    return render(request, 'item/home.html', context)


class ItemListView(ListView):
    model = Item
    template_name = 'item/home.html'       # <app>/<model>_<viewtype>.html
    context_object_name = 'items'
    ordering = ['name_item']
    paginate_by = 5


class ItemDetailView(DetailView):
    model = Item


class ItemCreateView(CreateView):
    model = Item
    fields = ['name_item', 'note']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ItemUpdateView(UpdateView):
    model = Item
    fields = ['name_item', 'note']


class ItemDeleteView(DeleteView):
    model = Item
    success_url = '/'


def about(request):
    return render(request, 'item/about.html', {'title': 'About'})
