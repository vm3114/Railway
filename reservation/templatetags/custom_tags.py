from django import template
from django.urls import reverse

register = template.Library()

@register.simple_tag
def coach_booking_url(coach, train_name, from_station, to_station):
    return reverse('booking', kwargs={
        'coachType': coach.coach_type,
        'trainName': train_name,
        'fromStation': from_station,
        'toStation': to_station,
    })