import re
from django import forms

class CreateOrderForm(forms.Form):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Введите ваше имя",
            }
        )
    )
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Введите вашу фамилию",
            }
        )
    )
    phone_number = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Введите ваш номер телефона",
            }
        )
    )
    requires_delivery = forms.ChoiceField(
        widget=forms.RadioSelect(
            attrs={
                "class": "form-check-input",
            }
        ),
        choices=[
            ("0", "Самовывоз"),
            ("1", "Требуется доставка"),
        ],
        initial="0",
    )
    delivery_address = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "id": "delivery-address",
                "rows": 2,
                "placeholder": "Введите адрес доставки",
            }
        ),
        required=False,
    )
    payment_on_get = forms.ChoiceField(
        widget=forms.RadioSelect(
            attrs={
                "class": "form-check-input",
            }
        ),
        choices=[
            ("0", "Оплата картой"),
            ("1", "Оплата наличными / картой при получении"),
        ],
        initial="1",
    )

    def clean_phone_number(self):
        data = self.cleaned_data["phone_number"]
        if not data.isdigit():
            raise forms.ValidationError("Номер телефона должен содержать только цифры.")
        
        pattern = re.compile(r"^\d{10,12}$")
        if not pattern.match(data):
            raise forms.ValidationError("Неверный формат номера телефона.")
        return data
