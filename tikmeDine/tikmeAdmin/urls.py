# tikmeReservation/urls.py
from django.urls import path
from .views import admin_dashboard

urlpatterns = [
    path('admin_dashboard/', admin_dashboard, name='admin_dashboard'),
    path('accounts/', include('authentication.urls')),
]
