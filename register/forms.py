from dataclasses import field
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

from django import forms

# import this model do as to connect the new fields to the userCreation form
from django.contrib.auth.models import user


#to modify the Django UserCreationform, inherite it from your class 
class RegisterForms(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = user
        # this field pattern shows how they will appear on the page
        fields = ['Useername', 'email', 'password1', 'password2']
