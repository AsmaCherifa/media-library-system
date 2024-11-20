from django import forms
from .models import Abonne, Document, Emprunt
from django.forms import DateInput

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
