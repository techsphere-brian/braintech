from django.db import models

# Create your models here.
class Student(models.Model):
   fname = models.CharField(max_length=50)
   lname = models.CharField(max_length=50)
   email = models.EmailField(max_length=100)
   age = models.PositiveIntegerField()
   phone = models.CharField(max_length=50)
   profile = models.ImageField(upload_to='profiles/')
   
   def __str__(self):
       return f'{self.fname}{self.lname}'