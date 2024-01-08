from django.db import models
from django.contrib.auth.models import User

# Create your models here.

DAYS = [
    ("MON", "Monday"),
    ("TUE", "Tuesday"),
    ("WED", "Wednesday"),
    ("THU", "Thursday"),
    ("FRI", "Friday"),
    ("SAT", "Saturday"),
    ("SUN", "Sunday"),
]

COACHES = [
    ("1A", "AC First Class"),
    ("2A", "AC Second Class"),
    ("3A", "AC Third Class"),
    ("SL", "Sleeper Class"),
    ("GN", "General Class"),
]

class DayOfWeek(models.Model):
    name = models.CharField(max_length=3, choices=DAYS)

    def __str__(self):
        return self.name

class Stop(models.Model):
    station = models.CharField(max_length = 50)
    time = models.TimeField()
    order = models.IntegerField(null = True) # 0 to (no. of stops - 1)

    def __str__(self):
        return f"{self.order}-{self.station}-{self.time}"

    class Meta:
        ordering = ['order']

class Train(models.Model):
    code = models.PositiveIntegerField()
    name = models.CharField(max_length = 100)
    stops = models.ManyToManyField(Stop, through = 'Train_stops')
    operating_days = models.ManyToManyField('DayOfWeek', blank=True)

    def __str__(self):
        return f"{self.code}-{self.name}"
    
    class Meta:
        ordering = ['code']

class Train_stops(models.Model):
    train = models.ForeignKey(Train, on_delete=models.CASCADE)
    stop = models.ForeignKey(Stop, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.train.name}-{self.stop}"
    
    class Meta:
        unique_together = ('train', 'stop')

class Coach(models.Model):
    code = models.CharField(max_length = 2)  # eg: A1, S8 etc
    coach_type = models.CharField(max_length = 2, choices = COACHES)
    total_seats = models.PositiveIntegerField()
    price_per_segment = models.IntegerField(default = 0)
    train = models.ForeignKey(Train, on_delete = models.CASCADE)

    def __str__(self):
        return f"Coach {self.code} in {self.train} ({self.coach_type})"
    
    class Meta:
        ordering = ['coach_type']
    
    def available_seats(self):
        booked_seats = 0    
        return max(0, self.total_seats - booked_seats)


class JourneySegment(models.Model):
    coach = models.ForeignKey(Coach, on_delete=models.CASCADE)
    order = models.IntegerField()  # eg: order = 2 represents journey from the Station with order 2 to the station with order 3 
    day = models.ForeignKey(DayOfWeek, on_delete = models.CASCADE)

    def __str__(self):
        return f"{self.coach.train} - Journey Segment {self.order} in coach {self.coach.code} on {self.day}"


class Seat(models.Model):
    number = models.CharField(max_length = 5)
    is_booked = models.BooleanField(default = False)
    journey_segment = models.ForeignKey(JourneySegment, on_delete = models.CASCADE, null = True)

    def __str__(self):
        status = "Booked" if self.is_booked else "Available"
        return f"Seat {self.number} in {self.journey_segment.coach.train} for Journey Segment {self.journey_segment.order} on {self.journey_segment.day} ({status})"
    
    class Meta:
        ordering = ['number']

    
class Account(models.Model):
    user = models.ForeignKey(User, on_delete = models.SET_NULL, null = True, blank = True)
    credit = models.IntegerField(default = 0)
    bookings = models.ManyToManyField(Seat, blank = True)
    email = models.EmailField(null = True)

    def __str__(self):
        return self.user.username
    

class Booking(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    seat = models.OneToOneField(Seat, on_delete=models.CASCADE)
    price = models.PositiveIntegerField()

    def __str__(self):
        return f"Booking for {self.account.user.username} - Seat {self.seat.number}"

class SeatReservation(models.Model):
    seat_number = models.CharField(max_length=5)
    coach = models.ForeignKey(Coach, on_delete=models.CASCADE)
    day = models.ForeignKey(DayOfWeek, on_delete=models.CASCADE)
    bookings = models.ManyToManyField(Booking)
    name = models.CharField(max_length = 255)
    age = models.PositiveIntegerField()
    date = models.DateField()

    def __str__(self):
        return f"Seat Reservation for Seat {self.seat_number} on {self.day} in {self.coach.train}"