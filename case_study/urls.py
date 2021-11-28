from . import views
from django.urls import path

urlpatterns = [
    path('case_study/', views.PostList.as_view(), name='case_study'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]