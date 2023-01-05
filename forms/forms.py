from django import forms

class registration(forms.Form):
    name=forms.CharField(initial="You Name",help_text="please enter your name") 
    email=forms.EmailField()   
    mobile=forms.IntegerField() 
    key=forms.CharField(widget=forms.HiddenInput)  
