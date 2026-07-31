from django import forms
from .models import BlogPost


class BlogForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ("title", "content", "preview", "views_count", "is_published")

    def __init__(self, *args, **kwargs):
        super(BlogForm, self).__init__(*args, **kwargs)
        self.fields["title"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите заголовок"}
        )
        self.fields["content"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите информацию"}
        )
        self.fields["views_count"].widget.attrs.update({"class": "form-control"})
        self.fields["preview"].widget.attrs.update({"class": "form-control"})
