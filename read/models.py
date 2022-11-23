from django.db import models

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    dob = models.DateField()
    email = models.EmailField(unique=True)
    country = models.CharField(max_length=30)

    def __str__(self):
        return self.first_name