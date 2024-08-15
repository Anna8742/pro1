from django.http import JsonResponse
from django.shortcuts import render
from .models import SessionLocal, Reservation
from datetime import datetime

def reservation_form(request):
    return render(request, 'reservations/form.html')

def create_reservation(request):
    if request.method == "POST":
        guest_name = request.POST.get('name')
        guest_count = request.POST.get('guest_count')
        reservation_date = request.POST.get('date')
        reservation_time = request.POST.get('time')

        db = SessionLocal()
        reservation = Reservation(
            guest_name=guest_name,
            guest_count=int(guest_count),
            reservation_date=datetime.strptime(reservation_date, '%Y-%m-%d'),
            reservation_time=reservation_time
        )
        db.add(reservation)
        db.commit()
        db.close()

        return JsonResponse({'message': 'Reservation successful'})
    return JsonResponse({'error': 'Invalid request'}, status=400)
