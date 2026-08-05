from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation.trans_real import catalog
from django.views import View
from django.views.generic import ListView, DetailView, TemplateView, DeleteView, CreateView, UpdateView
from .forms import ProductForm
from django.http import HttpResponseForbidden

from catalog.models import Product


class ContactsView(TemplateView):
    template_name = 'contacts.html'


class ProductListView(ListView):
    model = Product

    def get_queryset(self):
        return Product.objects.filter(is_published=True)


class ProductDetailView(DetailView):
    model = Product


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'catalog/catalog_confirm_delete.html'
    context_object_name = 'catalog'
    success_url = reverse_lazy('catalog:product_list')

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)

        is_moderator = self.request.user.has_perm('catalog.can_unpublish_product') or self.request.user.is_staff
        if obj.owner == self.request.user or is_moderator:
            return obj

        raise PermissionDenied("У вас нет прав на удаление этого продукта.")

class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
  #  fields = ('name', 'description', 'image', 'purchase_price', 'category') чтобы не забыть, заменили на форму
    success_url = reverse_lazy('catalog:product_list')

    def form_valid(self, form):

        form.instance.owner = self.request.user
        return super().form_valid(form)

class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)


        if obj.owner != self.request.user:
            raise PermissionDenied("Вы не являетесь владельцем этого продукта.")

        return obj



class UnpublishProductView(LoginRequiredMixin, View):
    def post(self, request, pk):
        product = get_object_or_404(Product, id=pk)

        if not  request.user.has_perm('catalog.can_unpublish_product'):
            return HttpResponseForbidden('У вас нет права на отмену публикации')

        product.is_published =False
        product.save()
        return redirect('catalog:product_list')
