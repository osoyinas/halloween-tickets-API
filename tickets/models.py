from django.db import models

class Ticket(models.Model):
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=15)
    email = models.EmailField()
    paid = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    companions = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)

