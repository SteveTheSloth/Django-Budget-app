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
from django.views.generic import UpdateView, DeleteView, CreateView, ListView
from .models import Transaction
from .views import (
    BalanceView,
    TransactionDetailView,
)


urlpatterns = [
    path("<int:monthyear>", BalanceView.as_view(queryset=Transaction.objects.all(), template_name="balance/balance.html"),
         name="balance"),
    path("", BalanceView.as_view(queryset=Transaction.objects.all(), template_name="balance/balance.html"),
         name="balance"),
    path("expenses", ListView.as_view(queryset=Transaction.objects.filter(transaction_type="Expense"),
                                      template_name="balance/expenses.html"), name="expenses"),
    path("incomes", ListView.as_view(queryset=Transaction.objects.filter(transaction_type="Income"),
                                     template_name="balance/incomes.html"), name="incomes"),
    path("loans", ListView.as_view(queryset=Transaction.objects.filter(transaction_type="Loan"),
                                   template_name="balance/loans.html"), name="loans"),
    path("details/<int:pk>/", TransactionDetailView.as_view(queryset=Transaction.objects.all(),
         template_name="balance/details.html"), name="details"),
    path("create", CreateView.as_view(
        model=Transaction, fields="__all__", template_name="balance/create.html"), name="create"),
    path("<int:pk>/update", UpdateView.as_view(queryset=Transaction.objects.all(),
         template_name="balance/update.html", fields="__all__"), name="update"),
    path("<int:pk>/delete", DeleteView.as_view(queryset=Transaction.objects.all(),
         template_name="balance/delete.html"), name="delete"),
]
