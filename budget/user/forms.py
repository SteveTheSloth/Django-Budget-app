from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db.models.fields import CharField


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
