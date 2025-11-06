from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .forms import ReservaionForm

def hellow_world(request): 
    return HttpResponse("Hello world")

class HellowEthiopia(View):
    def get(self ,  request):
        return HttpResponse("Hello Ethiopia")
    

def home(request):
    form = ReservaionForm()

    if request.method == 'POST':
        form = ReservaionForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("success")
        
        return render(request, 'index.html' , {'form' :  form})