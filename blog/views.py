from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from blog.models import BlogPost


# Контроллер для модели через CBV.
class HomeListView(ListView):
    model = BlogPost
    template_name = "blog/blog_list.html"


    def get_queryset(self):
        return BlogPost.objects.filter(is_published=True) # Публикуем только активные статьи


# Создание новой статьи.
class BlogCreateView(CreateView):
    model = BlogPost
    fields = ("title", "content", "preview", "views_count", "is_published")
    success_url = reverse_lazy('blog:home')


class BlogUpdateView(UpdateView):
    model = BlogPost
    fields = ("title", "content", "preview", "views_count", "is_published")

    def get_success_url(self):
        return reverse_lazy('blog:blog_detail', kwargs={'pk': self.object.pk}) # Возвращаем на статью.



class BlogDetailView(DetailView):
    model = BlogPost
    template_name = 'blog/blogpost_detail.html'
    context_object_name = 'blog'

    def get_object(self, queryset=None): # Подсчет просмотров.

        obj = super().get_object(queryset=queryset)
        obj.views_count += 1
        obj.save(update_fields=['views_count'])

        return obj
