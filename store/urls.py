from django.urls import path
from . import views

urlpatterns = [
    path('customer/', views.get_all_customers, name='customer-list'),
]