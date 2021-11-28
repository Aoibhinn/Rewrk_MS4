from . import views
from django.urls import path

urlpatterns = [
    path('case_study/', views.PostList.as_view(), name='case_study'),
]