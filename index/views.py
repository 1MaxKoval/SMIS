from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse 
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .models import Staff, Student, SchoolMember, Timetable
from .forms import LoginForm, StaffForm, PasswordForm, UserForm, TableForm
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required, user_passes_test
import pdb 

def index(request):
    if request.method == "GET":
        return render(request, 'index/index.html')

def login(request): 
    request.session.set_test_cookie()
    if request.session.test_cookie_worked() == False:
       return render(request, 'index/errors/sad_cookie.html')
    request.session.delete_test_cookie()
    if request.method == "POST":
        parsed_login = LoginForm(request.POST)
        if parsed_login.is_valid():
           u = authenticate(username=parsed_login.cleaned_data['username'], password=parsed_login.cleaned_data['password'])
           if u is not None:
               request.session['username'] = u.username
               request.session['password'] = parsed_login.cleaned_data['password']
               try:
                   if u.schoolmember.active == False:
                       u = Staff(user=u)
                       form = StaffForm(instance=u)
                       return render(request, 'index/login_process/model_form.html', {'form': form})
                   elif u.schoolmember.active == True:
                       return render(request, 'index/index.html')
               except ObjectDoesNotExist:
                   u = Staff(user=u)
                   u.save()
                   form = StaffForm(instance=u)
                   return render(request, 'index/login_process/model_form.html', {'form': form})
    elif request.method == "GET":
        try:
            request.session['username']
            return render(request, 'index/login_process/loggedin_page.html')
        except KeyError:
            form = LoginForm() 
            return render(request, 'index/login_process/login_form.html', {'form': form})

    return redirect('/profiles')

def model_form_submit(request):
    if request.method == "POST":
        data = StaffForm(request.POST) 
        if data.is_valid():
            user = User.objects.get(username=request.session['username'])
            user = Staff(user=user) 
            user.phoneNumber = data.cleaned_data['phoneNumber']
            user.address = data.cleaned_data['address']
            user.postCode = data.cleaned_data['postCode']
            user.email = data.cleaned_data['email']
            user.active = True
            user.save()
            return redirect('/profiles')
        data = UserForm(request.POST)
        if data.is_valid():
            user = User.objects.get(username=request.session['username'])
            user = Staff(user=user) 
            user.phoneNumber = data.cleaned_data['phoneNumber']
            user.address = data.cleaned_data['address']
            user.postCode = data.cleaned_data['postCode']
            user.email = data.cleaned_data['email']
            user.save()
        return redirect('/profiles')

def display_user(request, userName):
    if request.method == 'GET':
        try:
            user = authenticate(username=request.session['username'], password=request.session['password'])
        except KeyError:
            return redirect('/profiles/login')
        if user is not None:
            try:
                if user.timetable.active == False:
                    return redirect('/profiles/edit_table/')
            except ObjectDoesNotExist:
                table = Timetable(user=user)
                table.save()
                return redirect('/profiles/edit_table')
            if request.session['username'] == userName or user.schoolmember.canViewOthers == True:
                m_periods = list()
                t_periods = list()
                w_periods = list()
                th_periods = list()
                f_periods = list()
                for period, lesson in user.timetable.__dict__.items():
                    if period.startswith('m_'):
                        m_periods.append(lesson)
                    elif period.startswith('t_'):
                        t_periods.append(lesson)
                    elif period.startswith('w_'):
                        w_periods.append(lesson)
                    elif period.startswith('th_'):
                        th_periods.append(lesson)
                    elif period.startswith('f_'):
                        f_periods.append(lesson)

                data = { 'username': userName,
                        'phoneNumber' : user.schoolmember.phoneNumber, 
                        'email': user.schoolmember.email, 
                        'address': user.schoolmember.address, 
                        'postCode': user.schoolmember.postCode, 
                        'birthDate': user.schoolmember.birthDate,
                        'm_periods': m_periods,
                        't_periods': t_periods,
                        'w_periods': w_periods,
                        'th_periods': th_periods,
                        'f_periods': f_periods,
                        }
                return render(request, 'index/profiles/profile.html', data) 
            return redirect('/profiles')
        return redirect('/profiles/login')

def logout(request):
    if request.method == 'POST':
        request.session.flush()
        return redirect('/profiles')
    return redirect('/profiles')

def change_password(request):
    if request.method == 'POST':
        form = PasswordForm(request.POST)
        if form.is_valid():
            if request.session['password'] == form.cleaned_data['currentPassword']:
                if form.cleaned_data['requestPassword'] == form.cleaned_data['requestPassword1']:
                    user = User.objects.get(username=request.session['username'])
                    user.set_password(form.cleaned_data['requestPassword'])
                    user.save()
                    request.session['password'] = form.cleaned_data['requestPassword']
                    return redirect('/profiles')
                else:
                    error = 'Passwords do not match!'
            else:
                error = 'Wrong Password!'
            form = PasswordForm()
            return render(request, 'index/login_process/password_form.html', {'error':error, 'form':form})
    if request.method == 'GET':
        form = PasswordForm()
        return render(request,'index/login_process/password_form.html', {'form':form})

def change_user(request):
    if request.method == 'GET':
        user = User.objects.get(username=request.session['username'])
        form = UserForm(initial={'email':user.schoolmember.email, 'phoneNumber':user.schoolmember.phoneNumber, 'postCode':user.schoolmember.postCode, 'address':user.schoolmember.address})
        return render(request, 'index/profiles_edit.html', {'form':form})

def create_table(request):
    if request.method == 'GET': 
        user = User.objects.get(username=request.session['username'])
        form = TableForm(instance=user.timetable) 
        return render(request, 'index/tables/table_change.html', {'form':form})
    if request.method == 'POST':
       data = TableForm(request.POST)
       if data.is_valid(): 
           user = User.objects.get(username=request.session['username'])
           user = Timetable(user=user)
           user.m_period1 = data.cleaned_data['m_period1']
           user.m_period2 = data.cleaned_data['m_period2'] 
           user.m_period3 = data.cleaned_data['m_period3']
           user.m_period4 = data.cleaned_data['m_period4']
           user.m_period5 = data.cleaned_data['m_period5']
           user.m_period6 = data.cleaned_data['m_period6']
           user.m_period7 = data.cleaned_data['m_period7']
           user.m_period8 = data.cleaned_data['m_period8']
           user.m_period9 = data.cleaned_data['m_period9']
           user.m_period10 = data.cleaned_data['m_period10']
           user.t_period1 = data.cleaned_data['t_period1']
           user.t_period2 = data.cleaned_data['t_period2']
           user.t_period3 = data.cleaned_data['t_period3']
           user.t_period4 = data.cleaned_data['t_period4']
           user.t_period5 = data.cleaned_data['t_period5']
           user.t_period6 = data.cleaned_data['t_period6']
           user.t_period7 = data.cleaned_data['t_period7']
           user.t_period8 = data.cleaned_data['t_period8']
           user.t_period9 = data.cleaned_data['t_period9']
           user.t_period10 = data.cleaned_data['t_period10']
           user.w_period1 = data.cleaned_data['w_period1']
           user.w_period2 = data.cleaned_data['w_period2']
           user.w_period3 = data.cleaned_data['w_period3']
           user.w_period4 = data.cleaned_data['w_period4']
           user.w_period5 = data.cleaned_data['w_period5']
           user.w_period6 = data.cleaned_data['w_period6']
           user.w_period7 = data.cleaned_data['w_period7']
           user.w_period8 = data.cleaned_data['w_period8']
           user.w_period9 = data.cleaned_data['w_period9']
           user.w_period10 = data.cleaned_data['w_period10']
           user.th_period1 = data.cleaned_data['th_period1']
           user.th_period2 = data.cleaned_data['th_period2']
           user.th_period3 = data.cleaned_data['th_period3']
           user.th_period4 = data.cleaned_data['th_period4']
           user.th_period5 = data.cleaned_data['th_period5']
           user.th_period6 = data.cleaned_data['th_period6']
           user.th_period7 = data.cleaned_data['th_period7']
           user.th_period8 = data.cleaned_data['th_period8']
           user.th_period9 = data.cleaned_data['th_period9']
           user.th_period10 = data.cleaned_data['th_period10']
           user.f_period1 = data.cleaned_data['f_period1']
           user.f_period2 = data.cleaned_data['f_period2']
           user.f_period3 = data.cleaned_data['f_period3']
           user.f_period4 = data.cleaned_data['f_period4']
           user.f_period5 = data.cleaned_data['f_period5']
           user.f_period6 = data.cleaned_data['f_period6']
           user.f_period7 = data.cleaned_data['f_period7']
           user.f_period8 = data.cleaned_data['f_period8']
           user.f_period9 = data.cleaned_data['f_period9']
           user.f_period10 = data.cleaned_data['f_period10']
           user.active = True
           user.save()
           return redirect('/profiles')
