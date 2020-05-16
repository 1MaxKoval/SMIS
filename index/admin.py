from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Student, Staff, Timetable

admin.site.register(Student)
admin.site.register(Staff)
admin.site.register(Timetable)

