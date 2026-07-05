from django.contrib import admin
from django.urls import path

from catalog import views

urlpatterns = [
    path("admin/", admin.site.urls),

    path('', views.home, name='home'),

    path('contacts/', views.contacts, name='contacts'),
]