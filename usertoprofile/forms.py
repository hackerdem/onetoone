from django.contrib.auth.models import User
from django import forms

class RegisterForm(forms.ModelForm):
    occupation = forms.CharField()
    bio = forms.CharField()
    location = forms.CharField()
    class Meta:
        model = User 
        fields = ('username','email','first_name','last_name','password')