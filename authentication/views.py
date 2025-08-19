from django.shortcuts import render, redirect
from .forms import LoginForm
from django.urls import reverse
from django.http import Http404
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages


def login(request):
    form = LoginForm()
    return render(request, 'authentication/index.html', {
        'form': form,
        'form_action': reverse('authentication:login-done')
    })


def login_done(request):
    if not request.POST:
        raise Http404()

    form = LoginForm(request.POST)

    if form.is_valid():
        username = form.cleaned_data.get('username', '')
        password = form.cleaned_data.get('password', '')

        user = authenticate(
            username=username,
            password=password,
        )

        if user is not None:
            auth_login(request, user)
            return redirect(reverse('shortener:home'))
        else:
            messages.error(request, 'Invalid data')
    else:
        messages.error(request, 'Fill in all fields')

    return render(request, 'authentication/index.html', {
        'form': form,
        'form_action': reverse('authentication:login-done')
    })


def logout(request):
    auth_logout(request)
    messages.success(request, 'You have successfully logged out')
    return redirect('authentication:login')
