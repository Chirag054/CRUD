from django.db import models

# Create your models here.

choice = (
    ('Male', 'Male'),
    ('Female', 'Female')
)

class Employee(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=50, choices=choice, default='Male')
    dob = models.DateField(default='01/01/1990')

    def __str__(self):
        return self.first_name

