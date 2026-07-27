from django.contrib import admin
from blog.apps import BlogConfig
from blog.models import BlogPost


# Register your models here.
@admin.register(BlogPost)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "content", "is_published","views_count",)
    list_filter = ("is_published",)
    search_fields = ("title", "content",)
