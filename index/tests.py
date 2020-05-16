from django.test import TestCase, RequestFactory, Client
from django.contrib.auth.models import User
from .views import create_table
from .forms import TableForm
from .models import Timetable
import pdb
import random


class TimeTablePrototype(TestCase): 
    def setUp(self):
        days = ['m_', 't_', 'w_', 'th_', 'f_'] 
        periods = [day+'period'+str(num) for day in days for num in range(1,11)]
        self.data = {k:'Mathematics' for k in periods}
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='max', password='nicepassword')
        self.user.save()
        self.session = {'username':'max', 'password':'nicepassword'}
        table = Timetable(user=self.user)
        table.save()

    def test_table_fill(self):
        data = TableForm(self.data)
        user = User.objects.get(username='max')
        attrs = user.__dict__
        user = User.objects.get(username='max')
        timetable = Timetable(user=user)
        #Almost looks like the save() method does not work have a look at the old examples and try to find the problem.
        #Write up on the error that is being caused and type the data in statically.

            
class TimetableTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='max', password='nicepassword')
        self.user.save()
        self.table = Timetable(user=self.user)
        self.table.save()
        self.subjects = ['Biology', 'Free', 'Absent', 'Mathematics', 'Physics', 'Chemistry', 'Art', 'English', 'Design Techonology']

    def test_table_input(self):
        user = Timetable(user=self.user)
        user.m_period1 = random.choice(self.subjects)
        user.m_period2 = random.choice(self.subjects)
        user.m_period3 = random.choice(self.subjects)
        user.m_period4 = random.choice(self.subjects)
        user.m_period5 = random.choice(self.subjects)
        user.m_period6 = random.choice(self.subjects)
        user.m_period7 = random.choice(self.subjects)
        user.m_period8 = random.choice(self.subjects)
        user.m_period9 = random.choice(self.subjects)
        user.m_period10 =  random.choice(self.subjects)
        user.t_period1 = random.choice(self.subjects)
        user.t_period2 = random.choice(self.subjects)
        user.t_period3 = random.choice(self.subjects)
        user.t_period4 = random.choice(self.subjects)
        user.t_period5 = random.choice(self.subjects)
        user.t_period6 = random.choice(self.subjects)
        user.t_period7 = random.choice(self.subjects)
        user.t_period8 = random.choice(self.subjects)
        user.t_period9 = random.choice(self.subjects)
        user.t_period10 =  random.choice(self.subjects)
        user.w_period1 = random.choice(self.subjects)
        user.w_period2 = random.choice(self.subjects)
        user.w_period3 = random.choice(self.subjects)
        user.w_period4 = random.choice(self.subjects)
        user.w_period5 = random.choice(self.subjects)
        user.w_period6 = random.choice(self.subjects)
        user.w_period7 = random.choice(self.subjects)
        user.w_period8 = random.choice(self.subjects)
        user.w_period9 = random.choice(self.subjects)
        user.w_period10 =  random.choice(self.subjects)
        user.th_period1 =  random.choice(self.subjects)
        user.th_period2 =  random.choice(self.subjects)
        user.th_period3 =  random.choice(self.subjects)
        user.th_period4 =  random.choice(self.subjects)
        user.th_period5 =  random.choice(self.subjects)
        user.th_period6 =  random.choice(self.subjects)
        user.th_period7 =  random.choice(self.subjects)
        user.th_period8 =  random.choice(self.subjects)
        user.th_period9 =  random.choice(self.subjects)
        user.th_period10 =  random.choice(self.subjects)
        user.f_period1 = random.choice(self.subjects)
        user.f_period2 = random.choice(self.subjects)
        user.f_period3 = random.choice(self.subjects)
        user.f_period4 = random.choice(self.subjects)
        user.f_period5 = random.choice(self.subjects)
        user.f_period6 = random.choice(self.subjects)
        user.f_period7 = random.choice(self.subjects)
        user.f_period8 = random.choice(self.subjects)
        user.f_period9 = random.choice(self.subjects)
        user.f_period10 =  random.choice(self.subjects)
        user.save()
        user = User.objects.get(username='max')
        timetable = user.timetable
        pdb.set_trace() 
#Testing the form
#Create the user
#Create an empty table for the user
#Generate random data for the user
#Insert the data into the table
#Display the table

