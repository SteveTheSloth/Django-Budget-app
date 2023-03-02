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
from django.views.generic import MonthArchiveView
from django.urls import path, include
from home.views import HomeView
from balance.models import Transaction

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", HomeView.as_view(queryset=Transaction.objects.all(),
         template_name="home/home.html"), name="welcome"),
    path("<int:monthyear>", HomeView.as_view(queryset=Transaction.objects.all(),
         template_name="home/home.html"), name="welcome"),
    path("test/<int:year>/<int:month>/", MonthArchiveView.as_view(
        queryset=Transaction.objects.all(), date_field="due_date", month_format="%m", template_name="home/test.html", allow_future=True), name="test"),
    path("balance/", include("balance.urls")),
]
