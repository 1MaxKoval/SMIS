from django.db import models
from datetime import datetime 
from django.contrib.auth.models import User 

class SchoolMember(models.Model):
    active = models.BooleanField(default=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    birthDate = models.DateField(default='1212-12-12')
    phoneNumber = models.CharField(max_length=9, default='')
    address = models.CharField(max_length=100, default='')  
    postCode = models.CharField(max_length=100, default='')
    email = models.EmailField()
    canViewOthers = models.BooleanField(default=False)

class Student(SchoolMember):
    parentEmail = models.EmailField(blank=True)

class Staff(SchoolMember):
    CLEANER = 'CL'
    TEACHER = 'T'
    TEST = 'TE'
    ROLES = ( 
            (CLEANER, 'Cleaner'), 
            (TEACHER, 'Teacher'), 
            (TEST, 'Test'),
    )        
    
    CLASSES = (
            ('Year 9', 'Year 9'),
            ('Year 10', 'Year 10'),
            ('Year 11', 'Year 11'),
            ('Year 12', 'Year 12'),
            ('Year 13', 'Year 13'),
            ('', ''), 
        )
    role = models.CharField(max_length=2, choices=ROLES, default=TEST)

class Timetable(models.Model):

    PERIODS = (
            ('Free', 'Free'), 
            ('Absent', 'Absent'),
            ('Mathematics', 'Mathematics'), 
            ('Biology','Biology'),
            ('Physics', 'Physics'),
            ('Chemistry', 'Chemistry'),
            ('Art', 'Art'),
            ('English', 'English'),
            ('Design Technology', 'Design Technology'),
            ('', ''), 
        )
    CLASSES = (
            ('Year 9', 'Year 9'),
            ('Year 10', 'Year 10'),
            ('Year 11', 'Year 11'),
            ('Year 12', 'Year 12'),
            ('Year 13', 'Year 13'),
            ('', ''), 
       )

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    active = models.BooleanField(default=False)

days = ['m_', 't_', 'w_', 'th_', 'f_']
periods = [day+'period'+str(num) for day in days for num in range(1,11)]

for period in periods:
   Timetable.add_to_class(period, models.CharField(max_length=255, default='', choices=Timetable.PERIODS))
