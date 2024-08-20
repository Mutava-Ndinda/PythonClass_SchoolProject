from rest_framework import serializers
from student.models import Student
from teacher.models import Teacher
from course.models import Course
from classroom.models import Classroom
from classperiod.models import ClassPeriod

# Student Serializers
class MinimalStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'first_name', 'last_name', 'email']

class StudentSerializer(serializers.ModelSerializer):
    classes = serializers.StringRelatedField(many=True)
    courses = serializers.StringRelatedField(many=True)

    class Meta:
        model = Student
        fields = '__all__'

# Teacher Serializers
class MinimalTeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id', 'first_name', 'last_name', 'email']

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'

# Course Serializers
class MinimalCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'course_title', 'course_code']

class CourseSerializer(serializers.ModelSerializer):
    teacher = MinimalTeacherSerializer()
    
    class Meta:
        model = Course
        fields = '__all__'

# Classroom Serializers
class MinimalClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = ['id', 'class_name', 'class_code']

class ClassroomSerializer(serializers.ModelSerializer):
    teacher = MinimalTeacherSerializer()
    
    class Meta:
        model = Classroom
        fields = '__all__'

# ClassPeriod Serializers
class MinimalClassPeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassPeriod
        fields = ['id', 'title', 'date', 'start_time', 'end_time']

class ClassPeriodSerializer(serializers.ModelSerializer):
    course = CourseSerializer()
    classroom = ClassroomSerializer()
    teacher = MinimalTeacherSerializer()
    students = MinimalStudentSerializer(many=True)
    
    class Meta:
        model = ClassPeriod
        fields = '__all__'
