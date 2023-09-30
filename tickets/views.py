from rest_framework import generics
from .models import Ticket
from .serializers import TicketSerializer
from rest_framework.response import Response

class CreateTicketAPIView(generics.CreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer