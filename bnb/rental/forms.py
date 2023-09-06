from django import forms
from django.forms import ModelForm
from .models import *


class BnbForm (forms.ModelForm) :

    class Meta:
        model = Bnb
        fields = '__all__'


class UserForm (forms.ModelForm) :

    class Meta:
        model = User
        fields = '__all__'


class BookingForm (forms.ModelForm) :

    class Meta:
        model = Booking
        fields = '__all__'


class ReviewForm (forms.ModelForm):

    class Meta:
        model = Review
        fields = '__all__'
