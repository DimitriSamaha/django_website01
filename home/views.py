from django.contrib.auth import authenticate, login, logout
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.urls.base import reverse
from django.contrib.auth.forms import UserCreationForm

from .forms import CreateUserForm

# Create your views here.
def index(request):
    if not request.user.is_authenticated:     
        return render(request, 'home/index.html')
    else:
        return render(request, 'home/menu.html')

def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid:
            try:
                form.save()
                user = authenticate(request, username=request.POST["username"], password=request.POST["password1"]) 
                login(request, user)
                return redirect(reverse('home:index'))
            except:
                message = form.errors
                return render(request, 'home/register.html', {
                "form": form,
                "message": message
            })
    return render(request, 'home/register.html', {
        "form": form
    })


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse('home:index'))
        else:
            message = " Incorrect credentials! Please try again."
            return render(request, "home/login.html", {
                "message": message
            })
    else:
        return render(request, 'home/login.html')

def logout_view(request):
    logout(request)
    return render(request, 'home/index.html')
