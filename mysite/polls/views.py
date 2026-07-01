from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # processing - db, cache, rendering HTML template
    # print(type(request))
    # print(request.method)
    print(request.user)
    return HttpResponse("Hi, world. You're at polls index.")
