from django.db import models

# Create your models here.
class Teacher(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    gender = models.CharField(max_length=20)
    email = models.EmailField()
    code = models.PositiveSmallIntegerField()
    country = models.CharField(max_length=20)
    bio = models.TextField()
    age = models.PositiveSmallIntegerField()
    phone_number = models.CharField(max_length=20)
    teacher_salary = models.PositiveSmallIntegerField(default=0)
    hire_date = models.DateField()
    image = models.ImageField()
    def __str__(self):
        return f"{self.first_name} {self.last_name}"