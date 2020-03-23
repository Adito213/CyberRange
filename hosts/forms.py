from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
from django.views.generic import TemplateView
from django import forms
# from .models import Team
from .models import *


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', ]


class Description(forms.ModelForm):
    post = forms.CharField()

    class Meta:
        model = Logs
        fields = ('description',)