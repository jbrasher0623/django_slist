from django.urls import path
from .views import LatestListView  # , ListDetailView, ListCreateView, ListUpdateView, ListDeleteView
# from . import views

urlpatterns = [
    # path('', views.home, name='blog-home'),
    path('', LatestListView.as_view(), name='list-home'),

    # path('list/<int:pk>/', ListDetailView.as_view(), name='list-detail'),
    # path('list/new/', ListCreateView.as_view(), name='list-create'),
    # path('list/<int:pk>/update', ListUpdateView.as_view(), name='list-update'),
    # path('list/<int:pk>/delete', ListDeleteView.as_view(), name='list-delete'),
]
