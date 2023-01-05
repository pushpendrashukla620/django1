from django import forms

class registration(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
