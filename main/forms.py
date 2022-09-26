# from socket import fromshare
from tabnanny import check
# import _socket
# from _socket import *
from django import forms


class CreateNewList(forms.Form):
    name = forms.CharField(label="name", min_length=2, error_messages={"error": "name of length must be greater than 2"})
    check = forms.BooleanField()