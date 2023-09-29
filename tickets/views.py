from rest_framework import generics, status
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from .models import Ticket, Person
from .serializers import TicketSerializer


class CreateTicketAPIView(generics.CreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

CreateTicketFinalView = csrf_exempt(CreateTicketAPIView.as_view())
