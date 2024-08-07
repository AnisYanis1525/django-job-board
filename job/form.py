from .models import Apply, Job
from django import forms



class ApplyForm(forms.ModelForm):
    class Meta:
        model = Apply
        fields = ['name', "email", 'website', "cv", "letter"]
        
        


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = '__all__'
        exclude = ('slug', 'owner',)
               