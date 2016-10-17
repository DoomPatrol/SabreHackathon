from django.contrib import admin

from .models import Company, Agent, Customer, TripPreference, FlightPreference, HotelPreference, Activity, ActivityPreference, Trip, Theme

# Register your models here.
admin.site.register(Company)
admin.site.register(Agent)
admin.site.register(Customer)
admin.site.register(TripPreference)
admin.site.register(FlightPreference)
admin.site.register(HotelPreference)
admin.site.register(Activity)
admin.site.register(ActivityPreference)
admin.site.register(Trip)
admin.site.register(Theme)
