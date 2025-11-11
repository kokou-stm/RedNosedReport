from django.urls import path
from .views import analyze_reports

urlpatterns = [
    path('', analyze_reports, name='analyze_reports'),
]