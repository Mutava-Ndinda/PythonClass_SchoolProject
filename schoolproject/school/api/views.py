from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from student.models import Student
from teacher.models import Teacher
from course.models import Course
from classroom.models import Classroom
from classperiod.models import ClassPeriod
from .serializers import StudentSerializer, TeacherSerializer, CourseSerializer, ClassroomSerializer, ClassPeriodSerializer, MinimalStudentSerializer, MinimalTeacherSerializer, MinimalCourseSerializer, MinimalClassroomSerializer, MinimalClassPeriodSerializer
from datetime import timedelta

class StudentListView(APIView):
    def get(self, request):
        students = Student.objects.all()

        # Query Parameters - used for filtering data
        first_name = request.query_params.get("first_name")
        country = request.query_params.get("country")

        if first_name:
            students = students.filter(first_name=first_name)

        if country:
            students = students.filter(country=country)

        serializer = MinimalStudentSerializer(students, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StudentDetailView(APIView):
    def get(self, request, id):
        student = get_object_or_404(Student, id=id)
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    def put(self, request, id):
        student = get_object_or_404(Student, id=id)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        student = get_object_or_404(Student, id=id)
        student.delete()
        return Response(status=status.HTTP_202_ACCEPTED)

    def post(self, request, id):
        student = get_object_or_404(Student, id=id)
        action = request.data.get('action')

        if action == 'enroll':
            course_code = request.data.get("course_code")
            return self.enroll(student, course_code)
        
        elif action == 'add_to_class':
            class_id = request.data.get("class_id")
            return self.add_to_class(student, class_id)

        return Response({"error": "Invalid action"}, status=status.HTTP_400_BAD_REQUEST)

    def enroll(self, student, course_code):
        course = get_object_or_404(Course, id=course_code)
        student.courses.add(course)
        return Response({"message": f"Student {student.id} enrolled in course {course.id}"}, status=status.HTTP_200_OK)

    def add_to_class(self, student, class_id):
        classroom = get_object_or_404(Classroom, id=class_id)
        student.classes.add(classroom)
        return Response({"message": f"Student {student.id} added to class {classroom.id}"}, status=status.HTTP_200_OK)

class TeacherListView(APIView):
    def get(self, request):
        teachers = Teacher.objects.all()
        serializer = MinimalTeacherSerializer(teachers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TeacherDetailView(APIView):
    def get(self, request, id):
        teacher = get_object_or_404(Teacher, id=id)
        serializer = TeacherSerializer(teacher)
        return Response(serializer.data)

    def put(self, request, id):
        teacher = get_object_or_404(Teacher, id=id)
        serializer = TeacherSerializer(teacher, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        teacher = get_object_or_404(Teacher, id=id)
        teacher.delete()
        return Response(status=status.HTTP_202_ACCEPTED)

    def post(self, request, id):
        teacher = get_object_or_404(Teacher, id=id)
        action = request.data.get('action')

        if action == 'assign_course':
            course_id = request.data.get("course_id")
            return self.assign_course(teacher, course_id)
        
        elif action == 'assign_class':
            class_id = request.data.get("class_id")
            return self.assign_class(teacher, class_id)

        return Response({"error": "Invalid action"}, status=status.HTTP_400_BAD_REQUEST)

    def assign_course(self, teacher, course_id):
        course = get_object_or_404(Course, id=course_id)
        teacher.courses.add(course)
        return Response({"message": f"Teacher {teacher.id} assigned to course {course.id}"}, status=status.HTTP_200_OK)

    def assign_class(self, teacher, class_id):
        classroom = get_object_or_404(Classroom, id=class_id)
        classroom.teacher = teacher
        classroom.save()
        return Response({"message": f"Teacher {teacher.id} assigned to class {classroom.id}"}, status=status.HTTP_200_OK)

class CourseListView(APIView):
    def get(self, request):
        courses = Course.objects.all()
        serializer = MinimalCourseSerializer(courses, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CourseDetailView(APIView):
    def get(self, request, id):
        course = get_object_or_404(Course, id=id)
        serializer = CourseSerializer(course)
        return Response(serializer.data)

    def put(self, request, id):
        course = get_object_or_404(Course, id=id)
        serializer = CourseSerializer(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        course = get_object_or_404(Course, id=id)
        course.delete()
        return Response(status=status.HTTP_202_ACCEPTED)

class ClassroomListView(APIView):
    def get(self, request):
        classrooms = Classroom.objects.all()
        serializer = MinimalClassroomSerializer(classrooms, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ClassroomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ClassroomDetailView(APIView):
    def get(self, request, id):
        classroom = get_object_or_404(Classroom, id=id)
        serializer = ClassroomSerializer(classroom)
        return Response(serializer.data)

    def put(self, request, id):
        classroom = get_object_or_404(Classroom, id=id)
        serializer = ClassroomSerializer(classroom, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        classroom = get_object_or_404(Classroom, id=id)
        classroom.delete()
        return Response(status=status.HTTP_202_ACCEPTED)

class ClassPeriodListView(APIView):
    def get(self, request):
        date = request.query_params.get('date')
        teacher_id = request.query_params.get('teacher_id')
        course_id = request.query_params.get('course_id')

        periods = ClassPeriod.objects.all()

        if date:
            periods = periods.filter(date=date)

        if teacher_id:
            periods = periods.filter(teacher__id=teacher_id)

        if course_id:
            periods = periods.filter(course__id=course_id)

        serializer = MinimalClassPeriodSerializer(periods, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data

        # Retrieve related objects
        teacher = get_object_or_404(Teacher, id=data.get('teacher_id'))
        course = get_object_or_404(Course, id=data.get('course_id'))
        classroom = get_object_or_404(Classroom, id=data.get('classroom_id'))

        # Capacity check
        if ClassPeriod.objects.filter(
            classroom=classroom, 
            date=data.get('date'), 
            start_time__lt=data.get('end_time'), 
            end_time__gt=data.get('start_time')
        ).exists():
            return Response({"error": "Classroom is already booked for this time period."}, status=status.HTTP_400_BAD_REQUEST)

        # Create ClassPeriod
        class_period = ClassPeriod.objects.create(
            date=data.get('date'),
            start_time=data.get('start_time'),
            end_time=data.get('end_time'),
            course=course,
            classroom=classroom,
            teacher=teacher,
            title=data.get('title'),
            description=data.get('description'),
            capacity=data.get('capacity')
        )

        serializer = ClassPeriodSerializer(class_period)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class ClassPeriodDetailView(APIView):
    def get(self, request, id):
        period = get_object_or_404(ClassPeriod, id=id)
        serializer = ClassPeriodSerializer(period)
        return Response(serializer.data)

    def put(self, request, id):
        period = get_object_or_404(ClassPeriod, id=id)
        serializer = ClassPeriodSerializer(period, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        period = get_object_or_404(ClassPeriod, id=id)
        period.delete()
        return Response(status=status.HTTP_202_ACCEPTED)

class TimetableListView(APIView):
    def get(self, request):
        timetable = {}
        class_periods = ClassPeriod.objects.select_related('teacher', 'course', 'classroom').prefetch_related('students')

        for period in class_periods:
            day = period.date.strftime('%A')  # Get the full name of the day (e.g., Monday)
            if day not in timetable:
                timetable[day] = []

            timetable[day].append({
                "title": period.title,
                "course": period.course.course_title,
                "teacher": f"{period.teacher.first_name} {period.teacher.last_name}",
                "classroom": period.classroom.class_name,
                "start_time": period.start_time.strftime('%H:%M'),
                "end_time": period.end_time.strftime('%H:%M'),
                "students": [f"{student.first_name} {student.last_name}" for student in period.students.all()],
                "attendance_count": period.attendance_count,
                "description": period.description,
                "capacity": period.capacity,
            })

        return Response(timetable)
