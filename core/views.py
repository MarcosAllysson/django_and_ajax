from django.shortcuts import render
from .models import Profile
from django.http import JsonResponse, HttpResponse


# Create your views here.
def index(request):
    return render(request, 'core/index.html', {})


def form(request):
    return render(request, 'core/form.html', {})


def getProfiles(request):
    profiles = Profile.objects.all()

    return JsonResponse({
        'profiles': list(profiles.values())
    })


def create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        bio = request.POST.get('bio')

        try:
            new_profile = Profile(name=name, email=email, bio=bio)
            new_profile.save()

            return HttpResponse('New profile created successfully!')
        except Exception as error:
            print(error)
            return HttpResponse('An error occur, contact admin.')
