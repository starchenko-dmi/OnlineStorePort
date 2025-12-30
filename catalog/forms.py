from django import forms
from .models import Product



class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label="Имя")
    phone = forms.CharField(max_length=20, label="Телефон")
    message = forms.CharField(widget=forms.Textarea, label="Сообщение")


FORBIDDEN_WORDS = {
    'казино', 'криптовалюта', 'крипта', 'биржа',
    'дешево', 'бесплатно', 'обман', 'полиция', 'радар'
}

def contains_forbidden_words(text):
    if not text:
        return False
    # Приводим текст к нижнему регистру и проверяем каждое слово
    text_lower = text.lower()
    for word in FORBIDDEN_WORDS:
        if word in text_lower:
            return True
    return False


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'image', 'category', 'price']
        labels = {
            'name': 'Наименование',
            'description': 'Описание',
            'image': 'Изображение',
            'category': 'Категория',
            'price': 'Цена товара',
        }

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
        'class': 'form-control',
        'placeholder': 'Введите название продукта',
        })
        self.fields['description'].widget.attrs.update({
        'class': 'form-control',
        'placeholder': 'Введите описание',
        })
        self.fields['image'].widget.attrs.update({
        'class': 'form-control',
        })
        self.fields['category'].widget.attrs.update({
        'class': 'form-control',
        })
        self.fields['price'].widget.attrs.update({
        'class': 'form-control',
        })


    def clean_name(self):
        name = self.cleaned_data.get('name')
        if contains_forbidden_words(name):
            raise forms.ValidationError(
                "Название не должно содержать запрещённые слова: "
                "казино, криптовалюта, крипта, биржа, дешево, бесплатно, обман, полиция, радар."
            )
        return name

    def clean_description(self):
        description = self.cleaned_data.get('description')
        if contains_forbidden_words(description):
            raise forms.ValidationError(
                "Описание не должно содержать запрещённые слова: "
                "казино, криптовалюта, крипта, биржа, дешево, бесплатно, обман, полиция, радар."
            )
        return description

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price <= 0:
            raise forms.ValidationError('Стоимость товара должна быть больше 0')
        return price