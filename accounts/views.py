from django.shortcuts import render, redirect

from accounts.forms import CustomUserCreationForm

# Create your views here.
def index(request):
    return render(request, 'accounts/index.html')

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