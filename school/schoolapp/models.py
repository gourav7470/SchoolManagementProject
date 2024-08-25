from django.db import models 

# Create your models here.


class Student(models.Model):
  CLASS_CHOICES = [
        ('LKG', 'Lower Kindergarten'),
        ('UKG', 'Upper Kindergarten'),
        ('1', 'Class 1'),
        ('2', 'Class 2'),
        ('3', 'Class 3'),
        ('4', 'Class 4'),
        ('5', 'Class 5'),
        ('6', 'Class 6'),
        ('7', 'Class 7'),
        ('8', 'Class 8'),
        ('9', 'Class 9'),
        ('10', 'Class 10'),
        ('11', 'Class 11'),
        ('12', 'Class 12'),
    ]
  first_name = models.CharField(max_length=100)
  last_name = models.CharField(max_length=100)
  father_name = models.CharField(max_length=100)
  mother_name = models.CharField(max_length=100)
  email = models.CharField(max_length=100)
  dob = models.DateField()
  class_class = models.CharField(max_length=3,choices=CLASS_CHOICES,default='1')
  GENDER_CHOICES = [
      ('M', 'Male'),
      ('F', 'Female'),
      ('O', 'Other'),
      ('N', 'Prefer not to say'),
    ]
  gender = models.CharField(max_length=1,choices=GENDER_CHOICES,default='M')
  mobile = models.IntegerField()
  aadhar = models.IntegerField()
  address = models.TextField()
 
  def __str__ (self):
    return self.first_name
  

