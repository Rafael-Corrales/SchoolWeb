from django import forms
from .models import Mensaje

class MensajeForm(forms.ModelForm):
    class Meta:
        model = Mensaje
        fields = '__all__'
        widgets = {'remitente': forms.HiddenInput(),'leido': forms.HiddenInput()}