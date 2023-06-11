from django import forms
from .models import Clases

class ClasesForm(forms.ModelForm):
    class Meta:
        model = Clases
        fields = '__all__'
