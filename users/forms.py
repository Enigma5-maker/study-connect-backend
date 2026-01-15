from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Studyuser

class UserForm(UserCreationForm):
    class Meta:
        model = Studyuser
        fields = ('username', 'email', 'password1', 'password2')