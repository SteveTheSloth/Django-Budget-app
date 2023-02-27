from django.shortcuts import render
from balance.views import Transaction
from datetime import date
import calendar

# Create your views here.


month_str = str(date.today().month)
year_str = str(date.today().year)
month_year_int = int(month_str + year_str)


def welcome(request, monthyear=month_year_int):
    """The entire functionality relying on dates can and should be replaced by generic view classes
    MonthArchiveView...
    """
    if len(str(monthyear)) == 6:
        curr_year = int(str(monthyear)[-4:])
        curr_month = int(str(monthyear)[:2])
    else:
        curr_year = int(str(monthyear)[-4:])
        curr_month = int(str(monthyear)[:1])

    date_shown = date.today().replace(year=curr_year, month=curr_month)
    curr_month_weekday, curr_month_num_days = calendar.monthrange(
        curr_year, curr_month)

    # set values for previous and next month/year
    if date_shown.month not in (1, 12):
        prev_month = date_shown.month - 1
        next_month = date_shown.month + 1
        prev_year = curr_year
        next_year = curr_year
    elif date_shown.month == 1:
        prev_month = 12
        prev_year = curr_year - 1
        next_month = 2
        next_year = curr_year
    else:
        prev_month = 11
        prev_year = curr_year
        next_month = 1
        next_year = curr_year + 1

    next_month_int = int(str(next_month) + str(next_year))
    prev_month_int = int(str(prev_month) + str(prev_year))

    # Create list of tuples pairing transactions days(1-31) and transaction values
    dayly_transactions_dict = dict()
    for transaction in Transaction.objects.all():
        for key, value in transaction.day_balance(curr_month, curr_year).items():
            if key not in dayly_transactions_dict:
                dayly_transactions_dict[key] = [value]
            else:
                dayly_transactions_dict[key].append(value)

    transaction_tuples = [
        (i, None)
        if i not in dayly_transactions_dict
        else (i, dayly_transactions_dict.get(i))
        for i in range(1, curr_month_num_days + 1)
    ]

    # Create individual weeks for calendar to display.

    # Create list of last days of previous month that should be added on line 1 of calendar
    prev_month_num_days = calendar.monthrange(prev_year, prev_month)[1]
    last_days = [prev_month_num_days -
                 i for i in range(curr_month_weekday - 1, -1, -1)]

    first_week = [transaction_tuples[i] for i in range(7 - len(last_days))]
    second_week = [
        transaction_tuples[i] for i in range(first_week[-1][0], 14 - len(last_days))
    ]
    third_week = [
        transaction_tuples[i] for i in range(second_week[-1][0], 21 - len(last_days))
    ]
    fourth_week = [
        transaction_tuples[i] for i in range(third_week[-1][0], 28 - len(last_days))
    ]

    if fourth_week[-1][0] == curr_month_num_days:
        fifth_week = None
        sixth_week = None
    else:
        fifth_week = [
            transaction_tuples[i]
            for i in range(fourth_week[-1][0], len(transaction_tuples))
        ]

    if len(fifth_week) < 7:
        first_days = [i for i in range(1, 7) if len(fifth_week) + i <= 7]
        sixth_week = None
    elif fifth_week[-1][0] == curr_month_num_days:
        sixth_week = None
        first_days = None
    else:
        sixth_week = [
            transaction_tuples[i] for i in range(fifth_week[-1][0], 35 - len(last_days))
        ]
        first_days = [i for i in range(1, 7) if len(sixth_week) + i <= 7]

    return render(
        request,
        "home/home.html",
        {
            "month": date_shown.strftime("%B"),
            "year": curr_year,
            "next_month": next_month_int,
            "prev_month": prev_month_int,
            "last_days": last_days,
            "first_week": first_week,
            "second_week": second_week,
            "third_week": third_week,
            "fourth_week": fourth_week,
            "fifth_week": fifth_week,
            "sixth_week": sixth_week,
            "first_days": first_days,
        },
    )
