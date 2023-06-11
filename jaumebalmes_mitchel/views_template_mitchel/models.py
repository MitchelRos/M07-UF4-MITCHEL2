from django.db import models

# creacion modelos
class Clases(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.CharField(max_length=100)
    numberClass = models.IntegerField()
    students = models.IntegerField()
    classTutor = models.CharField(max_length=100)
    classPresident = models.CharField(max_length=100)
    description = models.TextField()
