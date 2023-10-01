from rest_framework import generics
from .models import Ticket, Person
from .serializers import TicketSerializer, PersonSerializer
from .permissions import IsStaffPermission
from django.shortcuts import render
import datetime

class CreateTicketAPIView(generics.CreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

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

