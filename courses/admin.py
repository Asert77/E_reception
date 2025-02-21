from django.contrib import admin
from .models import Enrollment, Course, Teacher, Timetable, Group


admin.site.register(Enrollment)
admin.site.register(Course)
admin.site.register(Teacher)
admin.site.register(Timetable)
admin.site.register(Group)