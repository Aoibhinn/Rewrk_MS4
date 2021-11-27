from django.urls import path
from . import views

urlpatterns = [
    path('', views.servicebooking, name="service_booking"),

]