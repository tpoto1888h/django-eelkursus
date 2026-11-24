from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Book(models.Model):
    pealkiri = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    zanr = models.CharField(max_length=100, null=True)
    saadavus = models.BooleanField(default=False)
