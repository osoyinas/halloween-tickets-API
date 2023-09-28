from django.db import models


class Ticket(models.Model):
    titular = models.CharField(max_length=100)
    number = models.CharField(max_length=15)
    email = models.EmailField()
    paid = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.titular)


class Person(models.Model):
    ticket = models.ForeignKey(Ticket, related_name='persons', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)