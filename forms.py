from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Event

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField()
    last_name = forms.CharField()

    class Meta:
        model = User
        fields = ['username','email','first_name','last_name','password1','password2']

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title','category','image']
