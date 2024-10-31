from django.contrib import admin
from .models import CourtBooking

# Register your models here.
class BookingList(admin.ModelAdmin):
    list_display = ("user","courts","day","time")

admin.site.register(CourtBooking, BookingList)