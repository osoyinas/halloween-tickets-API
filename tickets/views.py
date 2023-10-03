import datetime
from rest_framework import generics, status
from rest_framework.response import Response
from django.db.models import Q
from .models import Ticket, Person
from .serializers import TicketSerializer, PersonSerializer
from .permissions import IsStaffPermission
from django.shortcuts import render

class CreateTicketAPIView(generics.CreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    def create(self, request, *args, **kwargs):
        # Obtén los datos del ticket del cuerpo de la solicitud
        titular = request.data.get('titular')
        number = request.data.get('number')
        email = request.data.get('email')

        # Verifica si ya existe un ticket con la misma información
        existing_ticket = Ticket.objects.filter(Q(titular=titular) & Q(number=number) & Q(email=email)).first()

        if existing_ticket:
            # Si existe un ticket con la misma información, devuelve un error
            return Response({'error': 'Este ticket ya existe.'}, status=status.HTTP_400_BAD_REQUEST)
        return super().create(request, *args, **kwargs)
class CheckPersonAPIView(generics.RetrieveAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    permission_classes =[IsStaffPermission]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        
        previus_checked = instance.checked
        if not instance.checked and instance.ticket.paid:
            instance.checked = True
            instance.time_checked =  datetime.datetime.now().time()
            instance.save()



        context = {
            'id': instance.id,
            'person_name': instance.name,
            'ticket': instance.ticket,
            'checked': previus_checked,
            'time': instance.time_checked
        }

        print(context)
        return render(request, 'person_check.html', context)

