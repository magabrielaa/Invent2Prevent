from django.db import models

# Create your models here.

RACE_CHOICES = (
    ('White', 'White'),
    ('African American', 'African American'),
    ('Hispanic', 'Hispanic'),
    ('Other', 'Other'),
)

GENDER_CHOICES = (
    ('Female', 'Female'),
    ('Male', 'Male'),
)

AGE_CHOICES = (
    ('12-15', '12-15'),
    ('16-19', '16-19'),
    ('20-24', '20-24'),
    ('25-34', '25-34'),
    ('35-49', '35-49'),
    ('50-64', '50-64'),
    ('65+', '65+'),
)

class Input(models.Model):
    race = models.fields.CharField(max_length=50, choices=RACE_CHOICES, default="fill in your info")
    gender = models.fields.CharField(max_length=50, choices=GENDER_CHOICES, default="fill in your info")
    age = models.fields.CharField(max_length=50, choices=AGE_CHOICES, default="fill in your info")
    state = models.fields.CharField(max_length=50, default="fill in your info")
