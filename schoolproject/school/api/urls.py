from django.urls import path
from .views import (
    StudentListView,
    StudentDetailView,
    TeacherListView,
    TeacherDetailView,
    CourseListView,
    CourseDetailView,
    ClassroomListView,
    ClassroomDetailView,
    ClassPeriodListView,
    ClassPeriodDetailView,
    TimetableListView
)

urlpatterns = [
    path('students/', StudentListView.as_view(), name='student-list'),
    path('students/<int:id>/', StudentDetailView.as_view(), name='student-detail'),
    path('teachers/', TeacherListView.as_view(), name='teacher-list'),
    path('teachers/<int:id>/', TeacherDetailView.as_view(), name='teacher-detail'),
    path('courses/', CourseListView.as_view(), name='course-list'),
    path('courses/<int:id>/', CourseDetailView.as_view(), name='course-detail'),
    path('classrooms/', ClassroomListView.as_view(), name='classroom-list'),
    path('classrooms/<int:id>/', ClassroomDetailView.as_view(), name='classroom-detail'),
    path('classperiods/', ClassPeriodListView.as_view(), name='classperiod-list'),
    path('classperiods/<int:id>/', ClassPeriodDetailView.as_view(), name='classperiod-detail'),
    path('timetables/', TimetableListView.as_view(), name='timetable-list'),
]
