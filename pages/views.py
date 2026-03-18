from django.shortcuts import render
from .models import Profile
from .forms import ProfileForm
from django.shortcuts import redirect


def home(request):
    profiles = Profile.objects.all()   # fetch all rows
    context = {
        "profiles" : profiles
    }
    return render(request, 'pages/home.html' , context)


def about(request):
    return render(request, 'pages/about.html')

#Add profile form function :
def add_profile(request):

    if request.method == "POST":
        form = ProfileForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/')

    else:
        form = ProfileForm()

    return render(request, 'pages/add_profile.html', {'form': form})