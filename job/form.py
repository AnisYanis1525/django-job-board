from .models import Apply
from django import forms



class ApplyForm(forms.ModelForm):
    class Meta:
        model = Apply
        fields = ['name', "email", 'website', "cv", "letter"]
        
        