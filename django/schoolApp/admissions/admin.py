from django.contrib import admin
from admissions.models import StudentAdmissionModel
# Register your models here.
class StudentAdmissionModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'age',)  # Fields to display in the table
    list_filter = ('name',)  # Add filters on the right sidebar
    search_fields = ('name', 'age')  # Add search functionality

admin.site.register(StudentAdmissionModel, StudentAdmissionModelAdmin)
# admin.site.register(StudentAdmissionModel)