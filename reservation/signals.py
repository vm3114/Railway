from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from .models import *
from allauth.account.signals import user_logged_in



# It generates seats when a coach is created
@receiver(post_save, sender = Coach)
def create_journey_segments_and_seats(sender, instance, created, **kwargs):

    if created:
        train = instance.train
        stops = Train_stops.objects.filter(train = train).order_by('stop__order')
        operating_days = train.operating_days.all()        

        for day in operating_days:
            for i in range(len(stops) - 1):
                journey_segment = JourneySegment.objects.create(coach = instance, order = i, day = day)
                for seat_number in range(1, instance.total_seats + 1):
                    Seat.objects.create(
                        number = f"{instance.code}-{seat_number}",
                        is_booked = False,
                        journey_segment = journey_segment
                        )

# to refund user when booking deleted
@receiver(pre_delete, sender=Booking)
def refund_on_booking_delete(sender, instance, **kwargs):
    
    account = instance.account
    account.credit += instance.price
    account.save()
    seat = instance.seat
    seat.is_booked = False
    seat.save()

@receiver(user_logged_in)
def google_profile(sender, request, user, **kwargs):
    Account.objects.get_or_create(user=user, email=user.email)
