from django.shortcuts import render, redirect

from accounts.forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model
# Create your views here.
def index(request):
    user = get_user_model().objects.all()
    context = {
        'user' : user,
    }
    return render(request, 'accounts/index.html', context)

def signup(request):
    if request.method == 'POST':
        forms = CustomUserCreationForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('accounts:index')
    else:
        forms = CustomUserCreationForm()

    context = {
        'form':forms,
    }
    return render(request, 'accounts/signup.html', context)

def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('accounts:index')
    else:
        form = AuthenticationForm()
    context = {
        'form':form,
    }
        
    return render(request,'accounts/login.html', context)

def detail(request, user_pk):
    user = get_user_model().objects.get(pk=user_pk)
    context = {
        'user' : user,
    }
    return render(request, 'accounts/detail.html', context)

def update(request):
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('accounts:detail', request.user.pk)
    else:
        form = CustomUserChangeForm(instance=request.user)
    
    context = {
        'form':form,
    }

    return render(request, 'accounts/update.html', context)

def logout(request):
    auth_logout(request)
    return redirect('accounts:index')