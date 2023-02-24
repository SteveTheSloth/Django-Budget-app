from django.shortcuts import render
from balance.views import Transaction
from datetime import date

# Create your views here.


def welcome(request):

    curr_month = date.today().month
    curr_year = date.today().year
    dayly_expenses_dict = dict()
    dayly_incomes_dict = dict()

    for transaction in Transaction.objects.all():
        dayly_transactions_dict = transaction.day_balance(
            curr_month, curr_year)
        if transaction.type == "Expense":
            for key, value in dayly_transactions_dict.items():
                if key in dayly_expenses_dict:
                    dayly_expenses_dict[key].append(value)
                else:
                    dayly_expenses_dict[key] = [value]

        if transaction.type == "Income":
            for key, value in dayly_transactions_dict.items():
                if key in dayly_incomes_dict:
                    dayly_incomes_dict[key].append(value)
                else:
                    dayly_incomes_dict[key] = [value]

    return render(request, "home/home.html", {"expenses": dayly_expenses_dict.items(), "incomes": dayly_incomes_dict.items()})
