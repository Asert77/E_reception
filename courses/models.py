from django.db import models
from django.conf import settings


class Teacher(models.Model):
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    phone_number = models.CharField(max_length=15)
    course = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.course} o'qituvchisi. Tel: {self.phone_number}"


class Course(models.Model):
    title = models.CharField(max_length=255)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='courses')
    description = models.TextField(null=True)
    price =  models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title


class Enrollment(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    days = models.CharField(max_length=100)
    is_approved = models.BooleanField(default=False)
    enrolled_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('student', 'course')

        def __str__(self):
            return f"{self.student.phone_number} - {self.course.title}"


class Timetable(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="timetable")
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name="timetable")
    date = models.CharField(max_length=100)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return self.date


class Group(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="groups")
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name="groups")
    days = models.CharField(max_length=100)
    start_time = models.TimeField()
    end_time = models.TimeField()


    def __str__(self):
        return f"{self.course.title} - {self.days}"