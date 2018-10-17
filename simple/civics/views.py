from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Candidate
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import requests

def index(request):
    candidates = Candidate.objects.all
    return render(request, 'civics/index.html', {'candidates': candidates})


def getsenator(request):

    state = request.POST.get('state')
    r = requests.get("https://api.propublica.org/congress/v1/members/senate/"+str(request.POST[state])+"/current.json", headers=key)
    if r.status_code == 200:
        print(state)
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