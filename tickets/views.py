from rest_framework import generics
from .models import Ticket
from .serializers import TicketSerializer

class TicketListCreateView(generics.ListCreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

class TicketDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
