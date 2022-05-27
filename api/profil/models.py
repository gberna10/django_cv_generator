from django.db import models

# Create your models here.

class Profil(models.Model):
    gender = models.CharField(max_length=120)
    birthday = models.DateField()
    phone = models.CharField(max_length=120)
    mail = models.CharField(max_length=120)
    location = models.TextField()
    website = models.CharField(max_length=120)