from django.urls import path
from .views import CreateTicketAPIView

urlpatterns = [
    path('tickets/', CreateTicketAPIView.as_view(), name='ticket-list-create'),
]