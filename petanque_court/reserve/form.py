from django import forms 
from django.contrib.admin import widgets
from .models import CourtBooking

class CourtForm(forms.ModelForm):
    class Meta:
        model = CourtBooking

        fields = ['courts','day','time']