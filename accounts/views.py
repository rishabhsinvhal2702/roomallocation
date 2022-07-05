from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from accounts.forms import RegistrationForm, AccountAuthenticationForm

def registration_view(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            rollno = form.cleaned_data.get('rollno')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(rollno=rollno, password = raw_password)
            login(request, account)
            return redirect('rooms:room_list')
        else:
            context['registration_form'] = form
    else:
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, 'accounts/register.html', context)


def logout_view(request):
    logout(request)
    return redirect('home')


def login_view(request):
    context = {}

    user = request.user
    if user.is_authenticated:
        return redirect('rooms:room_list')

    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            rollno = request.POST['rollno']
            password = request.POST['password']
            user = authenticate(rollno=rollno, password=password)

            if user:
                login(request, user)
                return redirect('rooms:room_list')

        else:
            context['login_form'] = form

    else:
        form = AccountAuthenticationForm()
        context['login_form'] = form
    return render(request, 'accounts/login.html', context)
