from django.shortcuts import get_object_or_404
from .models import Category, Product


def get_products_by_category(category_id: int):
    """
    Возвращает категорию и список всех связанных с ней активных продуктов.
    """
    category = get_object_or_404(Category, id=category_id)


    products = Product.objects.filter(category=category, is_published =True)

    return category, products





