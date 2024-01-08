from django import template

register = template.Library()

@register.filter(name='coach_has_available_seats')
def coach_has_available_seats(coach):
    for journey_segment in coach.journeysegment_set.all():
        if journey_segment.seat_set.filter(is_booked=False).exists():
            return True
    return False

@register.simple_tag
def calculate_price(coach, to_stop, from_stop):
    return coach.price_per_segment * (to_stop.order - from_stop.order)