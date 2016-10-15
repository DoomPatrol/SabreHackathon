from django.shortcuts import render
from django.shortcuts import get_list_or_404, get_object_or_404

from .models import Agent, Customer

# Create your views here.
def the_dashboard(request):

    agent = get_object_or_404(Agent, user=request.user)
    customers = agent.customer_set.all()
    context = {'agent': agent, 'customers': customers}

    return render(request, 'app/dashboard.html', context)
