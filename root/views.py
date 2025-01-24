from django.shortcuts import render
from django.http import HttpResponse

def index(request) -> HttpResponse:
    # Hello, World!
    return HttpResponse("Hello, World!", status=202)
