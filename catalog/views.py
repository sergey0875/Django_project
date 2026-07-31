from django.urls import reverse_lazy
from django.utils.translation.trans_real import catalog
from django.views.generic import ListView, DetailView, TemplateView, DeleteView, CreateView, UpdateView
from .forms import ProductForm

from catalog.models import Product


class ContactsView(TemplateView):
    template_name = 'contacts.html'


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'catalog/catalog_confirm_delete.html'
    context_object_name = 'catalog'
    success_url = reverse_lazy('catalog:product_list')

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
  #  fields = ('name', 'description', 'image', 'purchase_price', 'category') чтобы не забыть, заменили на форму
    success_url = reverse_lazy('catalog:product_list')

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')