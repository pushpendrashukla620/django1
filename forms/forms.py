from django import forms

class registration(forms.Form):
    name=forms.CharField(initial="You Name",help_text="please enter your name") #this will set id as some_name ehere name is name of formfield 
    email=forms.EmailField() #this will set id as email which is name of formfield 
    text=forms.EmailField(  ) #this will set id as email which is name of formfield 
    next=forms.EmailField() #this will set id as email which is name of formfield 
