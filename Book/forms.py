from django import forms
from Book.models import book

class BookForm(forms.ModelForm):

    class Meta:
        model = book
        fields = ('__all__')

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price < 0:
            self.add_error('price','O preço deve ser maior que zero')
        return price
    
