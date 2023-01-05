from django.shortcuts import render
from .forms import registration
# Create your views here.

def showFormData(request):
    fm=registration()
    return render(request,"forms/registration.html" ,{"form":fm})