from tkinter.font import names

from django.urls import path, include
from .views import CourseListView, EnrolmentViewSets, TeacherView, TimetableListView, GroupListView
from rest_framework.routers import DefaultRouter
router = DefaultRouter()

router.register(r'courses',EnrolmentViewSets )


urlpatterns = [
    path('enrollment/', include(router.urls)),

    path('courses/', CourseListView.as_view(), name='Course-list'),
    path('teachers/', TeacherView.as_view(), name='teacher-list'),
    path('time/', TimetableListView.as_view(), name='time-list'),
    path('courses/<int:course_id>/groups/', GroupListView.as_view(), name='group-list')
]