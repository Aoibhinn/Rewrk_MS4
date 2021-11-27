from django.urls import path
from . import views


urlpatterns = [
    path('customer/', views.CustomerViewProfile.as_view(), name='customer')
]
