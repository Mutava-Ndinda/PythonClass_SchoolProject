from django.db import models
from classroom.models import Classroom 
from course.models import Course

class Student(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    student_code = models.PositiveSmallIntegerField()
    date_of_birth = models.DateField()
    country = models.CharField(max_length=20)
    bio = models.TextField()
    age = models.PositiveSmallIntegerField()
    phone_number = models.CharField(max_length=20)
    immediate_contact = models.CharField(max_length=20)
    image = models.ImageField()
    classes = models.ManyToManyField(Classroom, related_name='students')
    courses = models.ManyToManyField(Course, related_name='students')
    def __str__(self):
        return f"{self.first_name} {self.last_name}"