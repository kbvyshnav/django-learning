from django.shortcuts import render
from .models import Profile
from .forms import ProfileForm
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404


def home(request):
    profiles = Profile.objects.all()   # fetch all rows
    context = {
        "profiles" : profiles
    }
    return render(request, 'pages/home.html' , context)


def about(request):
    return render(request, 'pages/about.html')

######### Add profile form function : ################################
def add_profile(request):

    if request.method == "POST":
        form = ProfileForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/')

    else:
        form = ProfileForm()

    return render(request, 'pages/add_profile.html', {'form': form})

######### Update profile form function : ##############################
def update_profile(request, id):
    profile = get_object_or_404(Profile, id=id)

    if request.method == "POST":
        form = ProfileForm(request.POST, instance=profile)

        if form.is_valid():
            form.save()
            return redirect('/')

    else:
        form = ProfileForm(instance=profile)

    return render(request, 'pages/add_profile.html', {'form': form})

########### Delete Profile form func : #################################
def delete_profile(request, id):
    profile = get_object_or_404(Profile, id=id)
    profile.delete()
    return redirect('/')