from django import forms
from django.core.exceptions import ValidationError

from .models import Product

FORBIDDEN_WORDS = [
    "казино",
    "криптовалюта",
    "крипта",
    "биржа",
    "дешево",
    "бесплатно",
    "обман",
    "полиция",
    "радар",
]

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ("name", "description", "image", "purchase_price", "category")

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields["name"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите имя"}
        )
        self.fields["description"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите информацию"}
        )
        self.fields["category"].widget.attrs.update({"class": "form-control"})
        self.fields["image"].widget.attrs.update({"class": "form-control"})
        self.fields["purchase_price"].widget.attrs.update({"class": "form-control"})



    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get("name")
        description = cleaned_data.get("description")



        name_cleaned = name.lower().strip()
        description_cleaned = description.lower().strip()

        if name:

            for name_for in FORBIDDEN_WORDS:
                if name_for in name_cleaned:

                    self.add_error("name", f'Слово "{name}" нельзя применять!')
                    break

        if description:

            for description_for in FORBIDDEN_WORDS:
                if description_for in description_cleaned:
                    self.add_error(
                        "description", f'Слово "{description}" нельзя применять!'
                    )
                    break

        return cleaned_data

    def clean_purchase_price(self):
        purchase_price = self.cleaned_data.get("purchase_price")

        if purchase_price < 0:
            raise ValidationError("Цена не может быть отрицательной")
        elif purchase_price == 0:
            raise ValidationError("Цена не может быть нулевой")
        return purchase_price
