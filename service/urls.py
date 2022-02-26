"""
# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.ServiceList.as_view(), name='home'),
    path('<slug:slug>', views.ServiceDetail.as_view(), name='service_detail'),
]
