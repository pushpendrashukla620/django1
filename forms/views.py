from django.shortcuts import render
from .forms import registration
# Create your views here.

def showFormData(request):
    fm=registration(auto_id='some_%s', label_suffix="-",initial={'name':"merenam"})
    
     #this will set id as some_name ehere name is name of formfield 
     #auto_id can be set as True False also we can add any value like name_field
    return render(request,"forms/registration.html" ,{"form":fm})