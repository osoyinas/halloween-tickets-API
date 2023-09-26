from django.contrib import admin
from tickets.models import Ticket
# Register your models here.

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ['id', 'name','paid','formatted_price', 'number', 'email', 'date']
    def formatted_price(self, obj):
        # Formatea el precio con un símbolo de dólar ($) y dos decimales
        return f"{obj.price:.2f}Є"
    formatted_price.short_description = 'Precio'  # Define un encabezado personalizado para la columna
    search_fields = ['name', 'email'] 
    list_editable = ['paid']
    list_filter = ['paid']
    sortable_by = ['price']