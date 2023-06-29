from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Course, CourseSyllabus, Day, Syllabus


# for ImportExportModelAdmin sync.
class FilterSyllabus(ImportExportModelAdmin):
    filter_horizontal = ['syllabus']


# Register your models here.
admin.site.register(Course)
admin.site.register(CourseSyllabus, FilterSyllabus)
admin.site.register(Day)
admin.site.register(Syllabus)

# The End.
