from django.forms import ModelForm
from travelapp.models import Customer, Trip


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'email']

class TripForm(ModelForm):
    class Meta:
        model = Trip
        fields = ['depart_date', 'return_date', 'origin', 'destination']
