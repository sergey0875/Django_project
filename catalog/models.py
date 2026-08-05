from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="название")
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"
        ordering = ["name"]


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="название")
    description = models.TextField(null=True, blank=True, verbose_name="описание")
    image = models.ImageField(
        upload_to="photos/",
        blank=True,
        null=True,
        verbose_name="изображение",
        help_text="изображение продукта",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="products",
        verbose_name="категория",
    )
    purchase_price = models.IntegerField(verbose_name="цена закупки")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="дата создания")
    updated_at = models.DateTimeField(auto_now_add=True, verbose_name="дата изменения")
    is_published = models.BooleanField(default=False, verbose_name="опубликован")
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="products",
        verbose_name="владелец",
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"
        ordering = ["name"]
        permissions = [
            ('can_unpublish_product', 'can unpublish product')
        ]
