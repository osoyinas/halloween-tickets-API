from rest_framework import generics, status
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from .models import Ticket
from .serializers import TicketSerializer

@method_decorator(csrf_exempt, name='post')
class CreateTicketAPIView(generics.CreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

