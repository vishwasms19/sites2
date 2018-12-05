from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from authapp.forms import Userloginform
from django.contrib.auth.decorators import login_required
from formapp.forms import userforms


# Create your views here.
def userregistration(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
                name = form.cleaned_data['username']
                password = form.cleaned_data['password1']

                point = User()
                point.username = name
                point.set_password(password)
                point.save()
    return render(request,'registration.html', {'form':form})
def userlogin(request):
    form = Userloginform()
    message = ""
    if request.method == 'POST':
        form = Userloginform(request.POST)
        if form.is_valid():
            name = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(
                username=name,
                password= password
            )
            if user is None:
                message = 'invalid login details'
            else:
                login(request, user)
                request.session['city'] = 'bengaluru'
                request.session['address'] = 'btm'
                return redirect(dashboard)
    return render(request, 'login.html', {'form': form,'msg': message})

def dashboard(request):
    return render(request, 'dashboard.html')
def userlogout(request):
    logout(request)
    return redirect(userlogin)

def form(request):
    user = userforms()

    print(request.GET)

    if request.method == 'POST':
        user = userforms(request.POST)
        if user.is_valid():
            pass


    return render(request,'form.html',{'Form':user})