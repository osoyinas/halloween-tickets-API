from django.urls import path
from .views import CreateTicketAPIView


urlpatterns = [
    path('',  CreateTicketAPIView.as_view()),
]