from django import forms
from django.forms import ModelForm
from .models import Student, Staff, Timetable
from django.contrib.auth.models import User
import pdb

class LoginForm(forms.Form):
    username = forms.CharField(label='username', max_length=100)
    password = forms.CharField(label='password', max_length=100, widget=forms.PasswordInput)

class StaffForm(ModelForm):
    class Meta:
        model = Staff
        fields = ['phoneNumber', 'address', 'postCode', 'email']

class PasswordForm(forms.Form):
   currentPassword = forms.CharField(label='Current Password', max_length=100, widget=forms.PasswordInput)
   requestPassword = forms.CharField(label='New Password', max_length=100, widget=forms.PasswordInput)
   requestPassword1 = forms.CharField(label='Enter your new password again', max_length=100, widget=forms.PasswordInput)

class UserForm(forms.Form):
    phoneNumber = forms.CharField(label='Phone Number', max_length=9)
    email = forms.CharField(label='Email', max_length=100)
    postCode = forms.CharField(label='Post Code', max_length=100)
    address = forms.CharField(label='address', max_length=100)

class TableForm(ModelForm):
    class Meta:
        model = Timetable
        fields = [str(field).split('.')[-1:][0] for field in Timetable._meta.get_fields()[2:]]
