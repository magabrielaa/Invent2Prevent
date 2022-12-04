from django.db import models

# Create your models here.

class Input(models.Model):
    race = models.fields.CharField(max_length=50, default="fill in your info")
    gender = models.fields.CharField(max_length=50, default="fill in your info")
    age = models.fields.CharField(max_length=50, default="fill in your info")
    state = models.fields.CharField(max_length=50, default="fill in your info")

