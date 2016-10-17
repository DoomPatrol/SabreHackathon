from django.shortcuts import render
from django.shortcuts import get_list_or_404, get_object_or_404

from .forms import CustomerForm, TripForm

from .models import Agent, Customer

from . import myfilters


# Create your views here.
def the_dashboard(request):

    agent = get_object_or_404(Agent, user=request.user)
    customers = agent.customer_set.all()

    if request.method == 'POST':

        form = CustomerForm(request.POST)

        if form.is_valid():
            customer_create = form.save(commit=False)

            customer_create.agent = get_object_or_404(Agent, user=request.user)

            form.save()
    else:
        form = CustomerForm()

    context = {'agent': agent, 'customers': customers, 'form': form}

    return render(request, 'travelapp/dashboard.html', context)
