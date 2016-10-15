from tastypie import fields
from tastypie.resources import ModelResource
from .models import Agent, FlightPreference, Customer, HotelPreference, Theme

class AgentResource(ModelResource):
    class Meta:
        queryset = Agent.objects.all()
        resource_name = 'agent'

class CustomerResource(ModelResource):

    agent = fields.ForeignKey(AgentResource, 'agent')

    class Meta:
        queryset = Customer.objects.all()
        resource_name = 'customer'

class FlightPreferenceResource(ModelResource):
    customer = fields.ForeignKey(CustomerResource, 'customer')

    class Meta:
        queryset = FlightPreference.objects.all()
        resource_name = 'flightpreference'

class HotelPreferenceResource(ModelResource):
    customer = fields.ForeignKey(CustomerResource, 'customer')

    class Meta:
        queryset = HotelPreference.objects.all()
        resource_name = 'hotelpreference'

class ThemeResource(ModelResource):

    class Meta:
        queryset = Theme.objects.all()
        resource_name = 'theme'
