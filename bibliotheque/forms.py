from django import forms
from .models import Abonne, Document, Emprunt
from django.forms import DateInput
from django import forms
from django.core.exceptions import ValidationError
from .models import Emprunt
from datetime import date

class AbonneForm(forms.ModelForm):
    class Meta:
        model = Abonne
        fields = '__all__'

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = '__all__'
    date_publication = forms.DateField(widget=DateInput(attrs={'type': 'date'}))

class EmpruntForm(forms.ModelForm):
    class Meta:
        model = Emprunt
        fields = '__all__'

    date_emprunt = forms.DateField(widget=DateInput(attrs={'type': 'date'}))
    date_retour_prevue = forms.DateField(widget=DateInput(attrs={'type': 'date'}))

    def clean_date_emprunt(self):
        date_emprunt = self.cleaned_data.get('date_emprunt')
        if date_emprunt < date.today():
            raise ValidationError("La date d'emprunt ne peut pas être dans le passé.")
        return date_emprunt