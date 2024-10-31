from django.shortcuts import render, redirect
from datetime import datetime, timedelta
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.models import User
from .form import CourtForm
from .models import CourtBooking

def index(request):
    return render(request, "index_2.html",{})

def booking(request):
    form = CourtForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            save = form.save(commit=False)
            save.user = request.user
            if CourtBooking.objects.filter(courts=save.courts, day=save.day,time=save.time):
                messages.error(request, "มีการจองแล้ว กรุณาลองใหม่")
                return redirect('booking')
            else:
                save.save()
                messages.success(request,"การจองสนามสำเร็จ")
                return redirect('index')
        else:
            messages.info(request, 'Form error')
    return render(request, 'booking.html',{"form":form})

def userPanel(request):
    user = request.user
    courtbooking = CourtBooking.objects.filter(user=user).order_by('day', 'time')
    return render(request, 'userPanel.html', {
        'user':user,
        'courtbooking':courtbooking,
    })

def globalPanel(request):
    today = datetime.today()
    minDate = today.strftime('%Y-%m-%d')
    deltatime = today + timedelta(days=3)
    strdeltatime = deltatime.strftime('%Y-%m-%d')
    maxDate = strdeltatime
    #Only show the Courtbooked 3 days from today
    items = CourtBooking.objects.filter(day__range=[minDate, maxDate]).order_by('day', 'time')

    return render(request, 'globalPanel.html', {
        'items':items,
    })

def userUpdate(request, id):
    #Get booking id
    courtbooking = CourtBooking.objects.get(pk=id)

    #Instance of the form is the id
    form = CourtForm(request.POST, instance=courtbooking)
    if request.method == 'POST':
        if form.is_valid():
            save = form.save(commit=False)
            save.user = request.user
            if CourtBooking.objects.filter(courts=save.courts, day=save.day,time=save.time):
                messages.error(request, "มีการจองแล้ว กรุณาลองใหม่")
                return redirect('booking')
            else:
                #Update the existing booking
                save.save()
                messages.success(request,"การแก้การจองสนามสำเร็จ")
                return redirect('index')
        else:
            messages.info(request, 'Form error')
    return render(request, 'userUpdate.html',{"form":form})


