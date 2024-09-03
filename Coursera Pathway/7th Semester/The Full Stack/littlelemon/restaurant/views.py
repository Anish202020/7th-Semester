from django.shortcuts import render
from .models import Booking

def home(request):
    bookings = Booking.objects.all()
    print(bookings)
    
    context = {
        'bookings': bookings
    }
    
    return render(request, 'home.html', context)