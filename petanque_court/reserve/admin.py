from django.contrib import admin
from .models import Appointment

# Register your models here.
class BookingList(admin.ModelAdmin):
    list_display = ("user","service","day","time")

admin.site.register(Appointment, BookingList)