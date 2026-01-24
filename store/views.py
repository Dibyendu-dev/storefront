from django.shortcuts import render
from store.models import  Customer
# Create your views here.

def get_all_customers(request):
    # customers = Customer.objects.all()
    customers = Customer.objects.filter(membership=Customer.MEMBERSHIP_GOLD).order_by('first_name')
    return render(request, 'customer.html', {'customers': customers})