from  django.urls import path
from  django.contrib.auth.views import LoginView, LogoutView

from users.views import RegisterView, UserUpdateView

app_name = 'users'

urlpatterns = [
     path('register/', RegisterView.as_view(), name='register' ),
     path('login/', LoginView.as_view(template_name='users/login.html'), name= 'login' ),
     path('logout/', LogoutView.as_view(next_page='catalog:product_list'), name= 'logout'),
     path('users/update/', UserUpdateView.as_view(), name='users_update')

 ]