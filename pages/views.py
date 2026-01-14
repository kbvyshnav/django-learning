from django.shortcuts import render

# My views :

from django.http import HttpResponse

#function that returns a response/page
def home(request):
    return HttpResponse("Hello Vy 🐍, Welcome to Django!")

def about(request):
    return HttpResponse("This is the About page ✅")
