from django.db import models

class Ticket(models.Model):
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=15)
    email = models.EmailField()
    paid = models.BooleanField(default=False)

    def __str__(self):
        return str(self.name)

