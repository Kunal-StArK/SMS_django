from django.contrib import admin
from .models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name','roll_no','email','phone','course')
    list_filter=('roll_no','course')
    search_fields = ("roll_no",)

admin.site.register(Student,StudentAdmin)