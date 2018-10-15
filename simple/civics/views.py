from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Candidate
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import requests


def index(request):
    canidates = Candidate.objects.all
    return render(request, 'civics/index.html')


def getsenator(request):
    state = request.POST.get('state')
    if request.method == 'POST':
        r = requests.post("https://api.propublica.org/congress/v1/members/senate/" + request.POST[state] + "/current.json", data=request.GET, headers='key')
        r.json()
    else:
        r = requests.get("https://api.propublica.org/congress/v1/members/senate/" + request.POST[state] + "/current.json", params=request.GET, headers='key')
    if r.status_code == 200:
        return HttpResponseRedirect(reverse('civics:index'))



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