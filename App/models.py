from django.db import models
from django.forms import IntegerField

class Mama(models.Model):
    nombre = models.CharField(max_length=30)
    apodo = models.CharField(max_length=30)
    cumple = models.DateField()
    edad = models.IntegerField()

class Padrasto(models.Model):
    nombre = models.CharField(max_length=30)
    apodo = models.CharField(max_length=30)
    cumple = models.DateField()
    edad = models.IntegerField()

class Hermana(models.Model):
    nombre = models.CharField(max_length=30)
    apodo = models.CharField(max_length=30)
    cumple = models.DateField()
    edad = models.IntegerField()