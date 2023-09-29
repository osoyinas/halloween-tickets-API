from rest_framework import generics, status


from .models import Ticket
from .serializers import TicketSerializer

class CreateTicketAPIView(generics.CreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

