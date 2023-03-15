"""budget URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path, include
from django.views.generic import TemplateView
from home.views import (
    WelcomeView,
    registration,
    registration_group,
    login_group,
    success_group,
)
from balance.models import Transaction

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("", TemplateView.as_view(template_name="home/home.html"), name="home"),
    path(
        "welcome",
        login_required(
            WelcomeView.as_view(
                queryset=Transaction.objects.all(), template_name="home/welcome.html"
            )
        ),
        name="welcome",
    ),
    path(
        "welcome/<int:monthyear>",
        login_required(
            WelcomeView.as_view(
                queryset=Transaction.objects.all(), template_name="home/welcome.html"
            )
        ),
        name="welcome",
    ),
    path("registration/register", registration, name="sign_up"),
    path(
        "registration/register_group",
        login_required(registration_group),
        name="registration_group",
    ),
    path("registration/login_group", login_required(login_group), name="login_group"),
    path(
        "registration/success/<str:name>",
        login_required(success_group),
        name="success_group",
    ),
    path("balance/", include("balance.urls")),
]
