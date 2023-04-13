from django.db import models

# Crear BBDD de estudiantes
class Students(models.Model):
    name = models.CharField(max_length = 50)
    surname = models.CharField(max_length = 50)
    age = models.IntegerField()
    course = models.CharField(max_length = 100)
    birthdate = models.IntegerField()
    population = models.CharField(max_length = 50)

# Crear BBDD de profesores
class Teachers(models.Model):
    name = models.CharField(max_length = 50)
    surname = models.CharField(max_length = 50)
    age = models.IntegerField()
    subject = models.CharField(max_length = 50)
    birthdate = models.IntegerField()
    population = models.CharField(max_length = 50)
