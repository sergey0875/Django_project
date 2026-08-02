from django.urls import reverse_lazy
from django.views.generic import UpdateView
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm, CustomUserForm
from  django.core.mail import send_mail

from .models import CustomUser


class RegisterView(CreateView):
    template_name = 'users/register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('catalog:product_list')


    def form_valid(self, form):
        user = form.save()
        self.send_welcome_email(user.email)
        return super().form_valid(form)

    def send_welcome_email(self, user_email):
        subject = 'Добропожаловать!'
        message = ' Спасибо, что зарегистрировались в нашем маркетплейсе!'
        from_email = 'Serggg1205@yandex.ru'
        recipient_list = [user_email,]
        send_mail(subject, message, from_email, recipient_list)



class UserUpdateView(UpdateView):
    model = CustomUser
    form_class = CustomUserForm
    template_name = 'users/customuser_form.html'
    success_url = reverse_lazy('catalog:product_list')

    def get_object(self, queryset=None):
        return self.request.user

