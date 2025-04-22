# app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('summary/', views.summary_view, name='summary_view'),
]