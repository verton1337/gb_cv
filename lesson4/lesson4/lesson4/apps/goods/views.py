from django.shortcuts import render
from django.views.generic import ListView
from .models import Good
# Create your views here.



class MainView(ListView):
    model = Good
    template_name = "index.html"

        