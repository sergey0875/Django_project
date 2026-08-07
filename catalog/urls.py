from catalog.apps import CatalogConfig
from django.urls import path
from catalog.views import ContactsView, UnpublishProductView, CategoryProductsListView
from catalog.views import ProductListView, ProductDetailView, ProductDeleteView, ProductCreateView, ProductUpdateView

app_name = CatalogConfig.name

urlpatterns = [
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('', ProductListView.as_view(), name='product_list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('products/delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),
    path('products/create/', ProductCreateView.as_view(), name='product_create'),
    path('products/update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('products/unpublish/<int:pk>/', UnpublishProductView.as_view(), name='product_unpublish'),
    path('category/<int:category_id>/', CategoryProductsListView.as_view(), name='category_products'),

]
