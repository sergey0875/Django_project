from  django import forms
from django.contrib.auth.forms import UserCreationForm

from users.models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    phone_number = forms.CharField(max_length=15, required=False, help_text='Не обязательно для заполнения')
    username = forms.CharField(max_length=50, required=True)
    usable_password= None

    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'first_name', 'last_name', 'phone_number', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
            super(CustomUserCreationForm, self).__init__(*args, **kwargs)
            self.fields["email"].widget.attrs.update(
                {"class": "form-control", "placeholder": "Введите email"}
            )
            self.fields["username"].widget.attrs.update(
                {"class": "form-control", "placeholder": "Введите ник"}
            )
            self.fields["first_name"].widget.attrs.update({"class": "form-control", "placeholder": "Введите имя"})
            self.fields["last_name"].widget.attrs.update({"class": "form-control", "placeholder": "Введите Фамилию"})
            self.fields["phone_number"].widget.attrs.update({"class": "form-control", "placeholder": "Введите номер"})
            self.fields["password1"].widget.attrs.update({"class": "form-control", "placeholder": "Введите пароль"})
            self.fields["password2"].widget.attrs.update({"class": "form-control", "placeholder": "Повторите пароль"})


    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if phone_number and phone_number.isdigit():
            raise forms.ValidationError('Номер телефона должен состоять только из цифр')
        return phone_number


class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'phone_number','avatar', 'country')

    def __init__(self, *args, **kwargs):
            super(CustomUserForm, self).__init__(*args, **kwargs)
            self.fields["email"].widget.attrs.update(
                {"class": "form-control", "placeholder": "Введите email"}
            )
            self.fields["country"].widget.attrs.update(
                {"class": "form-control", "placeholder": "Введите Страну"}
            )
            self.fields["avatar"].widget.attrs.update({"class": "form-control"})
            self.fields["phone_number"].widget.attrs.update({"class": "form-control", "placeholder": "Введите номер телефона"})
            self.fields["username"].widget.attrs.update(
                {"class": "form-control", "placeholder": "Введите ник"})
