from django.contrib import admin
from tickets.models import Ticket,Person
from django.db import models
# Register your models here.

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ['id', 'titular','companions_count', 'paid','formatted_price', 'number', 'email', 'date']
    def formatted_price(self, obj):
        # Formatea el precio con un símbolo de dólar ($) y dos decimales
        return f"{obj.price:.2f}Є"
    
    def companions_count(self, obj):
        return obj.persons.count()
    companions_count.short_description = 'Personas'
    formatted_price.short_description = 'Precio'  # Define un encabezado personalizado para la columna
    search_fields = ['titular', 'email'] 
    list_editable = ['paid']
    list_filter = ['paid']
    sortable_by = ['price']

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'ticket_number', 'ticket_paid', 'ticket_contact', 'is_titular')  # Añade los atributos de Ticket que quieras mostrar

    def ticket_number(self, obj):
        return obj.ticket.id  # Reemplaza 'number' con el nombre del atributo en el modelo Ticket
    ticket_number.short_description = 'Ticket ID'  # Etiqueta que se mostrará en la columna

    def ticket_paid(self, obj):
        return "si" if obj.ticket.paid else "no"  # Reemplaza 'description' con el nombre del atributo en el modelo Ticket
    ticket_paid.short_description = 'Pagado'  # Etiqueta que se mostrará en la columna

    def ticket_contact(self, obj):
        return obj.ticket.number
    ticket_contact.short_description = 'Contacto'  # Etiqueta que se mostrará en la columna
    def is_titular(self,obj):
        return  "Titular" if obj.name == obj.ticket.titular else f"Acompañante de {obj.ticket.titular}"
 
    is_titular.short_description = 'titular'  # Etiqueta que se mostrará en la columna

            
