from __future__ import unicode_literals

from django.db import models
from django.conf import settings

import json


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
    airfare_cost = models.PositiveIntegerField(blank=True)
    airline = models.CharField(max_length=100, blank=True)
    depart_date = models.DateField(null=True)
    return_date = models.DateField(null=True)
    origin = models.CharField(max_length=3, null=True)
    destination = models.CharField(max_length=3, null=True)
    customer = models.ForeignKey(Customer)

    def __str__(self):

        return self.origin + ' ' + self.destination


class TripPreference(models.Model):
    trip_type = models.CharField(max_length=100, choices=TRIP_TYPES)
    customer = models.ForeignKey(Customer, null=True)

    def __str__(self):
        return self.trip_type

    @property
    def tojson(self):
        return json.dumps({
            "trip_type": self.trip_type
        })

class FlightPreference(models.Model):
    alliance = models.CharField(max_length=100, choices=ALLIANCE_CHOICES)
    seat = models.CharField(max_length=20, choices=SEAT_CHOICES)
    price = models.PositiveIntegerField()
    customer = models.ForeignKey(Customer)

    def __str__(self):
        return self.customer.name + ' flight preferences'

    @property
    def tojson(self):
        return json.dumps({
            "alliance": self.alliance,
            "seat": self.seat,
            "price": self.price
        })

class HotelPreference(models.Model):
    stars = models.PositiveIntegerField()
    hotel_type = models.CharField(max_length=40, choices=HOTEL_CHOICES)
    price = models.PositiveIntegerField()
    customer = models.ForeignKey(Customer)

    def __str__(self):
        return self.customer.name + ' hotel preferences'

    def tojson(self):
        return json.dumps({
            "stars": self.stars,
            "hotel_type": self.hotel_type,
            "price": self.price
        })


class Activity(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ActivityPreference(models.Model):
    activity = models.ManyToManyField(Activity)
    customer = models.ForeignKey(Customer, null=True)

    def __str__(self):
        return self.customer.name + ' activity preferences'

    @property
    def tojson(self):
        return json.dumps({
            "activity": self.activity
        })


class Theme(models.Model):
    name = models.CharField(max_length=100)
    customer = models.ForeignKey(Customer, null=True)

    def __str__(self):
        return self.name

    @property
    def tojson(self):
        return json.dumps({
            "theme": self.name
        })
