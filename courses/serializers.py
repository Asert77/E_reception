from rest_framework import serializers
from .models import Course, Enrollment, Teacher, Timetable


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class EnrollmentSerializer(serializers.ModelSerializer):
   student = serializers.StringRelatedField()

   class Meta:
        model = Enrollment
        fields = '__all__'


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'




class TimetableSerializer(serializers.ModelSerializer):
        course = serializers.StringRelatedField()
        teacher = serializers.StringRelatedField()

        class Meta:
            model = Timetable
            fields = ['id', 'course', 'teacher', 'date', 'start_time', 'end_time']