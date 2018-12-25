from django.urls import path
from .views import SupplierListView, SupplierDetailView, SupplierCreateView, SupplierUpdateView, SupplierDeleteView
from . import views

urlpatterns = [
    # path('', views.home, name='blog-home'),
    path('', SupplierListView.as_view(), name='supplier-home'),

    path('supplier/<int:pk>/', SupplierDetailView.as_view(), name='supplier-detail'),
    path('supplier/new/', SupplierCreateView.as_view(), name='supplier-create'),
    path('supplier/<int:pk>/update', SupplierUpdateView.as_view(), name='supplier-update'),
    path('supplier/<int:pk>/delete', SupplierDeleteView.as_view(), name='supplier-delete'),
    path('about/', views.about, name='supplier-about'),
]