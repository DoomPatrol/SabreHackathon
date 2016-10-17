from django.shortcuts import render, redirect
from django.shortcuts import get_list_or_404, get_object_or_404

from .models import Agent, Customer

from .forms import CustomerForm, TripForm

import requests

# Create your views here.
def the_dashboard(request):

    agent = get_object_or_404(Agent, user=request.user)
    customers = agent.customer_set.all()
    customer_form = C

    if request.method == 'POST':
        form = CustomerForm(request.POST)

        if form.is_valid():
            create_customer = form.save(commit=False)
            create_customer.agent = request.user

            form.save()
            return redirect(the_dashboard)
    else:
        form = CustomerForm()

    context = {'agent': agent, 'customers': customers, 'customer_form': form}

    return render(request, 'travelapp/dashboard.html', context)
