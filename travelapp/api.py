from tastypie import fields
from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from .models import Agent, FlightPreference, Customer, HotelPreference, Theme, TripPreference, Trip

class AgentResource(ModelResource):
    class Meta:
        queryset = Agent.objects.all()
        resource_name = 'agent'
        authorization = Authorization()

class CustomerResource(ModelResource):

    agent = fields.ForeignKey(AgentResource, 'agent')

    class Meta:
        queryset = Customer.objects.all()
        resource_name = 'customer'
        authorization = Authorization()

class FlightPreferenceResource(ModelResource):
    customer = fields.ForeignKey(CustomerResource, 'customer')

    class Meta:
        queryset = FlightPreference.objects.all()
        resource_name = 'flightpreference'
        authorization = Authorization()

class HotelPreferenceResource(ModelResource):
    customer = fields.ForeignKey(CustomerResource, 'customer')

    class Meta:
        queryset = HotelPreference.objects.all()
        resource_name = 'hotelpreference'
        authorization = Authorization()

class TripPreferenceResource(ModelResource):
    customer = fields.ForeignKey(CustomerResource, 'customer')

    class Meta:
        queryset = TripPreference.objects.all()
        resource_name = 'trippreference'
        authorization = Authorization()

class ThemeResource(ModelResource):

    class Meta:
        queryset = Theme.objects.all()
        resource_name = 'theme'
        authorization = Authorization()

class TripResource(ModelResource):

    customer = fields.ForeignKey(CustomerResource, 'customer')

    class Meta:
        queryset = Trip.objects.all()
        resource_name = 'trip'
        authorization = Authorization()
