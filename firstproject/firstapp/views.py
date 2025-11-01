from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

def hellow_world(request): 
    return HttpRespons("Hello world")

class HellowEthiopia(View):
    def get(self ,  request):
        return HttpResponse("Hello Ethiopia")