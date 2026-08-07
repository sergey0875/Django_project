from django.core.cache import cache

from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.views.generic import ListView, DetailView, TemplateView, DeleteView, CreateView, UpdateView
from .forms import ProductForm
from django.http import HttpResponseForbidden
from catalog.models import Product
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from .services import get_products_by_category



class ContactsView(TemplateView):
    template_name = 'contacts.html'




class ProductListView(ListView):
    model = Product

    def get_queryset(self):
        return Product.objects.filter(is_published=True)


    def get_queryset(self):
        """Низкоуровневое кэширование"""

        queryset = cache.get('my_queryset')
        if not queryset:
           queryset = super().get_queryset()
           cache.set('my_queryset', queryset, 60*15)
        return queryset




@method_decorator(cache_page(60*15), name='dispatch')
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

        if obj.owner != self.request.user and not self.request.user.is_staff:
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






class CategoryProductsListView(TemplateView):
    """
    Классовое представление для отображения продуктов в категории.
    """
    template_name = 'catalog/category_products.html'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        category_id = self.kwargs.get('category_id')

        category, products = get_products_by_category(category_id)

        context['category'] = category
        context['products'] = products

        return context

