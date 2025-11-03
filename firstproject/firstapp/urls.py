from django.urls import path 
from . import views

urlpatterns = [
    path('function' , views.hellow_world),
    path('class' , views.HellowEthiopia.as_view()),
]

