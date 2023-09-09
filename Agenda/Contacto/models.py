# Create your models here.
from django.db import models

# Create your models here.
class Contacto(models.Model):
    codigo=models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40)
    numero = models.CharField(max_length=60)
    email = models.EmailField(max_length=40)
