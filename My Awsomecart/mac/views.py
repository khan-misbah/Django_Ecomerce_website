from django.shortcuts import render
from django.http import HttpResponse
# Creat   e your views here.

def index(request):
        return render(request,"index.html")

    