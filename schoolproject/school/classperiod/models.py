from django.db import models
from student.models import Student
from course.models import Course
from classroom.models import Classroom
from teacher.models import Teacher

class ClassPeriod(models.Model):
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='class_periods')
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, related_name='class_periods')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='class_periods')
    students = models.ManyToManyField(Student, related_name='class_periods')
    attendance_count = models.PositiveSmallIntegerField(default=0)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    capacity = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"{self.title} - ({self.date})"