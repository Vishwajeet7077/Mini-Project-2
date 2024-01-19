# forms.py
from django import forms
from .models import RiskData

class RiskDataForm(forms.ModelForm):  # Rename the form class to avoid the conflict
    class Meta:
        model = RiskData
        fields = ['name']
