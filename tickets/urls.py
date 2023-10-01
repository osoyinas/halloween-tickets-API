from django.urls import path
from .views import CreateTicketAPIView, CheckPersonAPIView


urlpatterns = [
    path('',  CreateTicketAPIView.as_view()),
    path('check/<int:pk>/',CheckPersonAPIView.as_view())
]