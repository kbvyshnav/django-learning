from django.shortcuts import render


def home(request):
    context = {
        "name" : "Vy",
        "role" : "Python Developer",
        "day" : 7,
        "status" : "Learning Django consistently 💪"
    }
    return render(request, 'pages/home.html' , context)


def about(request):
    return render(request, 'pages/about.html')
