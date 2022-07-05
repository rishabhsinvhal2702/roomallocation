from logging import PlaceHolder
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from accounts.models import Account

class RegistrationForm(UserCreationForm):
    rollno = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'placeholder': 'Roll Number', 'class':'signup-field'}))
    phone = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'placeholder': 'Phone Number', 'class':'signup-field'}))
    email = forms.EmailField(max_length=60, widget=forms.TextInput(attrs={'placeholder': 'E-mail', 'class':'signup-field'}))
    first_name = forms.CharField(max_length=51, widget=forms.TextInput(attrs={'placeholder': 'First Name', 'class':'signup-field signup-fname'}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Last Name', 'class':'signup-field signup-lname'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password', 'class':'signup-field'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Confirm Password', 'class':'signup-field'}))

    class Meta:
        model = Account
        fields = ("rollno", "first_name", "last_name", "email", "phone", "password1", "password2")


class AccountAuthenticationForm(forms.ModelForm):
    rollno = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'placeholder': 'Roll Number', 'class':'login-field'}))
    password = forms.CharField(label='password', widget=forms.PasswordInput(attrs={'placeholder':'Password', 'class':'login-field'}))
    
    class Meta:
        model = Account
        fields = ('rollno', 'password')

    def clean(self):
        if self.is_valid():
            rollno = self.cleaned_data['rollno']
            password = self.cleaned_data['password']
            if not authenticate(rollno=rollno, password=password):
                raise forms.ValidationError('Invalid Login')