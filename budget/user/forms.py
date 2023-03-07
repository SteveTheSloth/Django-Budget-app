from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db.models.fields import CharField
from django.forms import ModelForm, Form
from django import forms
from .models import UserGroup


class RegistrationForm(UserCreationForm):
    auto_id = True

    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "email",
                  "username", "password1", "password2"]
        # field_classes = {"username": CharField}


class LoginForm(AuthenticationForm):
    class Meta:
        model = User


class GroupRegistrationForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = UserGroup
        exclude = ["admin", "members", "nr_of_members"]
        # fields = ["name", "password"]


class GroupLoginForm(Form):
    name = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput, max_length=35)
