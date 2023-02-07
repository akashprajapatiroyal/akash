import email
from django.db import models
from django.forms import CharField

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()

#for displaying name instead of contact object in database
    def __str__(self):
        return self.name
    