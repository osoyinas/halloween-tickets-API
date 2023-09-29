from rest_framework import generics, status
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .models import Ticket, Person
from .serializers import TicketSerializer


class CreateTicketAPIView(generics.CreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [AllowAny]

CreateTicketFinalView = csrf_exempt(CreateTicketAPIView.as_view())
