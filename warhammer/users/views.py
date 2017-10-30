from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render
from django.views.generic import FormView, ListView, CreateView
from .models import User


def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)


def logout_view(request):
    logout(request)


class UserListView(ListView):
    model = User
    template_name = 'userlist.html'
    context_object_name = 'users'


class SignUpView(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'user.html'
    success_url = 'users:userlist'
