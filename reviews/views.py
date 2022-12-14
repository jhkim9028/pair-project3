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

def update(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    if request.method == 'POST':
        review_form = ReviewForm(request.POST, instance=review)
        if review_form.is_valid():
            review_form.save()
            return redirect('reviews:detail', review.pk)
    else :
        review_form = ReviewForm(instance=review)
    context = {
        'review' : review,
        'review_form' : review_form,
    }
    return render(request,'reviews/update.html', context)

def delete(request,review_pk):
    Review.objects.get(pk=review_pk).delete()
    return redirect('reviews:index')