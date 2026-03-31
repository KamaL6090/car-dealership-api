from django.db import models

class Dealer(models.Model):
    name = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)

    def __str__(self):
        return self.name