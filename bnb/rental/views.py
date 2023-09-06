

from django.shortcuts import render, redirect
from .forms import *
from .models import *


def bnb_create(request):
    if request.method == 'POST':
        form = BnbForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bnb_list')
    else:
        form = BnbForm()
    return render(request, 'rental/bnb_create.html', {'form': form})

def bnb_list(request):
    bnbs = Bnb.objects.all()
    return render(request, 'rental/bnb_list.html', {'bnbs': bnbs})

def user_create(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserForm()
    return render(request, 'rental/user_create.html', {'form': form})

def user_list(request):
    users = User.objects.all()
    return render(request, 'rental/user_list.html', {'users': users})

def booking_create(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('booking_list')
    else:
        form = BookingForm()
    return render(request, 'rental/booking_create.html', {'form': form})

def booking_list(request):
    bookings = Booking.objects.all()
    return render(request, 'rental/booking_list.html', {'bookings': bookings})

def review_create(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('review_list')
    else:
        form = ReviewForm()
    return render(request, 'rental/review_create.html', {'form': form})

def review_list(request):
    reviews = Review.objects.all()
    return render(request, 'rental/review_list.html', {'reviews': reviews})

# Create your views here.
