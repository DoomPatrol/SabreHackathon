from __future__ import unicode_literals

from django.db import models
from django.conf import settings

# Create your models here.
ALLIANCE_CHOICES = (
    ('*A', 'Star Alliance'),
    ('*O', 'One World'),
    ('*S', 'Sky Team'),

)

SEAT_CHOICES = (
    ('WINDOW', 'Window'),
    ('AISLE', 'Aisle'),
    ('MIDDLE', 'Middle'),
)

HOTEL_CHOICES = (
    ('BUDGET', 'Budget'),
    ('MID', 'Mid'),
    ('SPLURGE', 'Splurge'),
)

TRIP_TYPES = (
    ('BUSINESS', 'Business'),
    ('LEISURE', 'Leisure'),
)
class Company(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Agent(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    company = models.ForeignKey(Company)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(null=True)
    agent = models.ForeignKey(Agent)

    def __str__(self):
        return self.name

class Trip(models.Model):
    customer = models.ForeignKey(Customer)
    hotel_cost = models.PositiveIntegerField()
    hotel = models.CharField(max_length=100)
    airfare_cost = models.PositiveIntegerField()
    arifare = models.CharField(max_length=100)


class TripPreference(models.Model):
    trip_type = models.CharField(max_length=100, choices=TRIP_TYPES)
    customer = models.ForeignKey(Customer, null=True)

    def __str__(self):
        return self.trip_type

class FlightPreference(models.Model):
    alliance = models.CharField(max_length=100, choices=ALLIANCE_CHOICES)
    seat = models.CharField(max_length=20, choices=SEAT_CHOICES)
    price = models.PositiveIntegerField()
    customer = models.ForeignKey(Customer)

    def __str__(self):
        return self.customer.name + ' flight preferences'

class HotelPreference(models.Model):
    stars = models.PositiveIntegerField()
    hotel_type = models.CharField(max_length=40, choices=HOTEL_CHOICES)
    price = models.PositiveIntegerField()
    customer = models.ForeignKey(Customer)

    def __str__(self):
        return self.customer.name + ' hotel preferences'


class Activity(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ActivityPreference(models.Model):
    activity = models.ManyToManyField(Activity)
    customer = models.ForeignKey(Customer, null=True)

    def __str__(self):
        return self.customer.name + ' activity preferences'

class Theme(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ThemePreference(models.Model):
    theme = models.ManyToManyField(Theme)
    customer = models.ForeignKey(Customer, null=True)

    def __str__(self):
        return self.customer.name + ' theme preferences'
