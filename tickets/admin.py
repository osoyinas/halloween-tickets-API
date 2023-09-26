from django.contrib import admin
from tickets.models import Ticket
# Register your models here.

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ['id', 'name','paid','price', 'number', 'email', 'date']
    search_fields = ['name', 'email'] 