from django.db import models

# Create your models here.

class Input(models.Model):
    race = models.fields.CharField(max_length=50, default="prefer not to answer")
    gender = models.fields.CharField(max_length=50, default="prefer not to answer")
    age = models.fields.CharField(max_length=50, default="prefer not to answer")

