from django import forms
from .models import Job

class Login_form(forms.ModelForm):
    class Meta:
        model = Job
        fields = '__all__'
        exclude = ['slug', 'user']