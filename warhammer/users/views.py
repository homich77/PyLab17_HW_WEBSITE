from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .forms import *
from django.shortcuts import render, redirect


def login_view(request):
    form = LoginForm(request.POST or None)
    if request.POST and form.is_valid():
        user = form.login(request)
        if user:
            login(request, user)
            return redirect('category_list')
    context = {'form': form, }
    return render(request, 'signup.html', context)


@login_required(login_url=reverse_lazy('login'))
def logout_view(request):
    logout(request)
    return redirect('category_list')


def signup_view(request):
    form = SignupForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password1')
        user.set_password(password)
        user.save()
        if user is not None:
            login(request, user)
            return redirect('category_list')
    context = {'form': form, }
    return render(request, 'signup.html', context)
