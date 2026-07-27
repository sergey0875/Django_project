from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    content = models.TextField(null=True, blank=True, verbose_name='Содержимое')
    preview = models.ImageField(
        upload_to="photos/",
        blank=True,
        null=True,
        verbose_name="изображение",
        help_text="изображение продукта",
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="дата создания")
    is_published = models.BooleanField(verbose_name='признак публикации')
    views_count = models.PositiveIntegerField(default=0, verbose_name='количество просмотров')

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = "Публикация"
        verbose_name_plural = "Публикации"
        ordering = ["title"]





