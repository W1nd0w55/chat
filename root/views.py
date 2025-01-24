from django.shortcuts import render
from django.http import HttpResponse

def index(request) -> HttpResponse:
    # Hello, World!
    return render(request, 'home.html')
