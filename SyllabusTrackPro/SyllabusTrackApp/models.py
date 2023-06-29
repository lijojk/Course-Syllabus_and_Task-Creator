from django.db import models


# creating Course model
class Course(models.Model):
    course = models.CharField(max_length=150)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.course

    class Meta:
        verbose_name_plural = "Course"


# creating Day model

class Day(models.Model):
    day = models.IntegerField(verbose_name="Days")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.day


# creating Syllabus model
class Syllabus(models.Model):
    syllabus = models.CharField(max_length=150)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.syllabus

    class Meta:
        verbose_name_plural = "Syllabus"


# creating CourseSyllabus model
class CourseSyllabus(models.Model):
    course = models.OneToOneField(Course, on_delete=models.CASCADE)
    day = models.OneToOneField(Day, on_delete=models.CASCADE)
    syllabus = models.ManyToManyField(Syllabus)
    Percentage = models.CharField(max_length=150)

    class Meta:
        verbose_name_plural = "Course Syllabus"
