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
from django.contrib.auth.decorators import login_required
from .models import Transaction
from .views import (
    BalanceView,
    TransactionDetailView,
    ExpenseListView,
    IncomeListView,
    LoanListView,
    create_transaction_view,
)


urlpatterns = [
    path("<int:monthyear>", BalanceView.as_view(template_name="balance/balance.html"),
         name="balance"),
    path("", BalanceView.as_view(template_name="balance/balance.html"),
         name="balance"),
    path("expenses", ExpenseListView.as_view(
        template_name="balance/expenses.html"), name="expenses"),
    path("incomes", IncomeListView.as_view(
        template_name="balance/incomes.html"), name="incomes"),
    path("loans", LoanListView.as_view(
        template_name="balance/loans.html"), name="loans"),
    path("details/<int:pk>/", TransactionDetailView.as_view(
         template_name="balance/details.html"), name="details"),
    path("create", create_transaction_view, name="create"),
    path("<int:pk>/update", login_required(UpdateView.as_view(model=Transaction,
         template_name="balance/update.html", fields="__all__")), name="update"),
    path("<int:pk>/delete", login_required(DeleteView.as_view(model=Transaction,
         template_name="balance/delete.html")), name="delete"),
]
