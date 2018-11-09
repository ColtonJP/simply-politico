from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import CurrentCongress
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import requests


def index(request):
    candidates = CurrentCongress.objects.all
    return render(request, 'civics/index.html', {'candidates': candidates})


def get_senator(request, state, house):
    candidate = CurrentCongress.objects.filter(state=state, house=house)
    return render(request, 'civics/detail.html', {'candidate': candidate})


def get_candidate(request):
    address = request.POST.get('address')
    state = request.POST.get('state1')
    incumbents = CurrentCongress.objects.filter(state=state)
    r = requests.get("https://www.googleapis.com/civicinfo/v2/voterinfo?key=              &address="+address+""+state+"")
    if r.status_code == 200:
        data = r.json()['contests']
        return render(request, 'civics/candidate.html', {'data': data, 'incumbents': incumbents})
    else:
        r = requests.get("https://www.googleapis.com/civicinfo/v2/representatives?key=              &address=" + address + "" + state + "")
        data = r.json()['officials']
        return render(request, 'civics/candidate.html', {'data': data, 'incumbents': incumbents})


def get_statement(request):
    key = {"X-API-Key": ""}
    bioguide_id = request.POST['statement']
    candidate = CurrentCongress.objects.filter(bioguide_id=bioguide_id)
    r = requests.get("https://api.propublica.org/congress/v1/members/"+bioguide_id+"/statements/115.json",
                 headers=key)
    if r.status_code == 200:
        data = r.json()['results'][0:5]
        r = requests.get("https://api.propublica.org/congress/v1/members/"+bioguide_id+"/bills/introduced.json",
                     headers=key)
        bills = r.json()['results']
        r = requests.get("https://api.open.fec.gov/v1/names/candidates/?api_key= &q=Patty%20Murray")
        contributions = r.json()
        return render(request, 'civics/statement.html', {'bills': bills, 'data': data, 'candidate': candidate, 'contributions':contributions})


def register_user(request):
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    user = User.objects.create_user(username, email, password)
    login(request, user)
    return HttpResponseRedirect(reverse('civics:index'))


def login_page(request):
    return render(request, 'civics/login.html')


def my_login(request):
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
