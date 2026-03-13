from django.shortcuts import render
from .models import Profile

def home(request):
    profiles = Profile.objects.all()   # fetch all rows
    context = {
        "profiles" : profiles
    }
    return render(request, 'pages/home.html' , context)


def about(request):
    return render(request, 'pages/about.html')
