from blog.apps import BlogConfig
from  django.urls import path
from .views import HomeListView, BlogCreateView, BlogDetailView, BlogUpdateView, BlogDeleteView

app_name = BlogConfig.name

urlpatterns = [
    path('blogs/', HomeListView.as_view(), name='home'),
    path('blogs/create/', BlogCreateView.as_view(), name= 'home_create' ),
    path('blogs/<int:pk>/', BlogDetailView.as_view(), name= 'blog_detail'),
    path('blogs/update/<int:pk>/', BlogUpdateView.as_view(), name= 'blog_update'),
    path('blogs/delete/<int:pk>/', BlogDeleteView.as_view(), name='blog_delete')

]
