from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login
from django.urls import reverse_lazy
from .forms import UserForm

class SignUpView(CreateView):
    form_class = UserForm
    template_name = 'users/signup.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response

class UserLoginView(LoginView):
    template_name = 'users/login.html'

    def form_valid(self, form):
        remember = self.request.POST.get('remember_me')
        if remember:
            self.request.session.set_expiry(60*60*24*30)
        else:
            self.request.session.set_expiry(0)
        return super().form_valid(form)

class UserLogoutView(LogoutView):
    next_page = reverse_lazy('login')
