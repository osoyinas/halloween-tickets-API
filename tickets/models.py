from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from .email import send_ticket_to_titular

class Ticket(models.Model):
    titular = models.CharField(max_length=100)
    number = models.CharField(max_length=15)
    email = models.EmailField()
    paid = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.titular)

@receiver(post_save, sender=Ticket)
def send_ticket_email(sender, instance, **kwargs):
    print("PAGADO")
    if instance.paid:
        send_ticket_to_titular(instance)


class Person(models.Model):
    ticket = models.ForeignKey(Ticket, related_name='persons', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)