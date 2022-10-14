from django.shortcuts import render, redirect
from .forms import ReviewForm
from .models import Review

# Create your views here.
def index(request):
    reviews = Review.objects.all()
    context = {
        'reviews':reviews,
    }
    return render(request, 'reviews/index.html', context)

def create(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reviews:index')
    else:
        form = ReviewForm()

    context = {
        'form':form,
    }
    return render(request, 'reviews/create.html', context)

def detail(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    context = {
        'review':review,
    }
    return render(request, 'reviews/detail.html', context)