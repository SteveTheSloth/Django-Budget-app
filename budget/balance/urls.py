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
from django.urls import path
from .views import balance, bills, details, incomes, lent, form


urlpatterns = [
    path("", balance, name="balance"),
    path("bills", bills, name="bills"),
    path("<int:id>", details, name="details"),
    path("incomes", incomes, name="incomes"),
    path("lent", lent, name="lent"),
    path("form", form, name="form"),
]
