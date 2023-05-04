from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Room(models.Model):
    number = models.CharField(max_length=10)
    def __str__(self):
        return self.number
    

class Vacancies(models.Model):
    date_start = models.DateField(auto_now=False, auto_now_add=False)
    date_end = models.DateField(auto_now=False, auto_now_add=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ManyToManyField(Room)
    def __str__(self):
        return f"{self.user} | room : {self.room}"
    