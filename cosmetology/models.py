from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    bio = models.TextField()

    def __str__(self):
        return self.name

class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Procedure(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    appointment_time = models.DateTimeField()

    def __str__(self):
        return self.name
