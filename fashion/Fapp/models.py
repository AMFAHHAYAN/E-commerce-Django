from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Resetuid(models.Model):
    Uuid = models.UUIDField(unique=True)
    user=models.ForeignKey(User, on_delete= models.CASCADE)
    expiry= models.DateTimeField()