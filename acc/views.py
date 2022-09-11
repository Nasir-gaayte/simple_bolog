from django.shortcuts import render,redirect
from .forms import RegisterUserForm
from django.contrib.auth import login, logout,authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

# Create your views here.


def register_request(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=True)
            login(request, user)
            messages.success(request,'wellcome')
            return redirect('home')
        else:
            messages.error(request,'something go wrongs')
            return redirect('register')
    form = RegisterUserForm()
    return render(request,'acc/register.html',{
        'register_form':form,
    })    


def login_req(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request,'wellcome')
                return redirect('home')
            else:
                messages.error(request,'wrong????')
                return redirect('login')
    form = AuthenticationForm()
    return render(request,"acc/login.html",{
        'login_form':form,
    })            
    

def logout_request(request):
    logout(request)
    return redirect('home')    