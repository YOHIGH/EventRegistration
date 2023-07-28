from django.shortcuts import render, HttpResponse
from .forms import *
from .models import *

# Create your views here.
def formsPage(request):
    if request.method == "POST":
        forms = UserForm(request.POST)
        if forms.is_valid():
            forms.save()
            return render(request, 'forms.html', {"forms": forms})
        
    else:
        forms = UserForm()
    
    return render(request, 'forms.html', {"forms": forms})