from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Candidate
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import requests


def index(request):
    candidates = CurrentCongress.objects.all
    return render(request, 'civics/index.html', {'candidates': candidates})


def get_senator(request):
    state = request.POST['state']
    house = request.POST['house']
    candidate = CurrentCongress.objects.filter(state=state, house=house)
    return render(request, 'civics/detail.html', {'candidate': candidate})


def get_statement(request):

    bioguide_id = request.POST.get('bioguide_id')
    house = request.POST.get('house')
    r = requests.get("https://api.propublica.org/congress/v1/members/C000127/statements/115.json",
                 headers=key)
    if r.status_code == 200:
        print(r.json())
        return HttpResponse(r.text)
# return HttpResponseRedirect(reverse('civics:index'))


def register_user(request):
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    user = User.objects.create_user(username, email, password)
    login(request, user)
    return HttpResponseRedirect(reverse('civics:index'))


def login_page(request):
    return render(request, 'civics/login.html')


def mylogin(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse('civics:index'))
    else:
        return HttpResponseRedirect(reverse('civics:login'))


@login_required(login_url='http://localhost:8000/civics/login/')
def logout_view(request):
    logout(request)
    return render(request, 'civics/logout.html')
