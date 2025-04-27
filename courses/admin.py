from django.contrib import admin
from .models import Enrollment, Course, Teacher, Group


admin.site.register(Enrollment)
admin.site.register(Course)
admin.site.register(Teacher)
admin.site.register(Group)