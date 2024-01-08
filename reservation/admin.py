from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Coach)
admin.site.register(Seat)
admin.site.register(Account)
admin.site.register(JourneySegment)
admin.site.register(DayOfWeek)
admin.site.register(Train)
admin.site.register(Stop)
admin.site.register(Train_stops)
admin.site.register(Booking)
admin.site.register(SeatReservation)