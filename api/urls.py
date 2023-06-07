# api/urls.py

from django.urls import path
from .views import get_UVI

urlpatterns = [
    path('UVI/<str:areaNo>/', get_UVI, name='get_UVI'),
]