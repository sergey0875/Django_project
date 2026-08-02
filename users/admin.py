from django.contrib import admin
from .models import CustomUser

@admin.register(CustomUser)
class UsersAdmin(admin.ModelAdmin):
    list_display = ("id", "country", "avatar", "phone_number","email",)
    search_fields = ("phone_number", "country",)
