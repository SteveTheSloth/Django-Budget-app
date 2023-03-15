from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import ModelForm, Form
from django import forms
from .models import MyUser, UserGroup


class RegistrationForm(UserCreationForm):
    auto_id = True

    class Meta:
        model = MyUser
        fields = [
            "id",
            "first_name",
            "last_name",
            "email",
            "username",
            "password1",
            "password2",
        ]


class LoginForm(AuthenticationForm):
    class Meta:
        model = MyUser


class GroupRegistrationForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = UserGroup
        exclude = ["admin", "members", "nr_of_members"]


class GroupLoginForm(Form):
    name = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput, max_length=35)
