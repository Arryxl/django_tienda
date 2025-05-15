from django.db import models

# Create your models here.
class Usuario(models.Model):
    usuario = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    
    def __str__(self):
        return self.usuario
    
from django.db import models