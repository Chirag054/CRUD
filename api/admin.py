from django.contrib import admin
from .models import Employee

# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id','first_name','last_name','age','gender')
    search_fields = ('id','first_name','last_name','age','gender')

admin.site.register(Employee, EmployeeAdmin)