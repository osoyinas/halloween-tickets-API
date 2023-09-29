from django.urls import path
from .views import CreateTicketFinalView

urlpatterns = [
    path('tickets/', CreateTicketFinalView, name='ticket-list-create'),
]