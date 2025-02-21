from rest_framework import generics, permissions, viewsets, filters
from rest_framework.response import Response
from .models import Course, Enrollment, Teacher, Timetable, Group
from .serializers import CourseSerializer, GroupSerializer, EnrollmentSerializer, TeacherSerializer, TimetableSerializer


class CourseListView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticated]


class EnrolmentViewSets(viewsets.ModelViewSet):
    serializer_class = EnrollmentSerializer
    queryset = Enrollment.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(student=self.request.user)


class TeacherView(generics.ListAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [permissions.IsAuthenticated]




class TimetableListView(generics.ListAPIView):
    queryset = Timetable.objects.all()
    serializer_class = TimetableSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupListView(generics.ListAPIView):
    serializer_class = GroupSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['days']
    search_fields = ['days']

    def get_queryset(self):
        course_id = self.kwargs['course_id']
        return Group.objects.filter(course_id=course_id)