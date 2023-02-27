from django.shortcuts import redirect, render, get_object_or_404

# Create your views here.

from datetime import date
from .models import Transaction
from .form import TransactionForm

month_str = str(date.today().month)
year_str = str(date.today().year)
month_year_int = int(month_str + year_str)


def balance(request, monthyear=month_year_int):
    """Same functionality as balance, takes monthyear=int(myyyy/mmyyyy) as argument to display month in past
    or future."""

    amount = 0
    if len(str(monthyear)) == 6:
        show_year = int(str(monthyear)[-4:])
        show_month = int(str(monthyear)[:2])
    else:
        show_year = int(str(monthyear)[-4:])
        show_month = int(str(monthyear)[:1])

    date_shown = date.today().replace(year=show_year, month=show_month)

    if show_month not in (1, 12):
        next_month = date_shown.replace(month=show_month + 1)
        prev_month = date_shown.replace(month=show_month - 1)
    elif show_month == 12:
        next_month = date_shown.replace(year=show_year + 1, month=1)
        prev_month = date_shown.replace(month=show_month - 1)
    else:
        next_month = date_shown.replace(month=2)
        prev_month = date_shown.replace(year=show_year - 1, month=12)

    next_month_int = int(str(next_month.month) + str(next_month.year))
    prev_month_int = int(str(prev_month.month) + str(prev_month.year))

    for transaction in Transaction.objects.all():
        amount += transaction.active_month(date_shown.month, date_shown.year)

    return render(
        request,
        "balance/balance.html",
        {
            "amount": amount,
            "month": date_shown.strftime("%B"),
            "year": date_shown.strftime("%Y"),
            "next_month": next_month_int,
            "prev_month": prev_month_int,
        },
    )


def bills(request):
    return render(
        request, "balance/bills.html", {
            "transactions": Transaction.objects.all()}
    )


def delete_check(request, id):
    transaction = get_object_or_404(Transaction, pk=id)
    transaction_type = transaction.type

    if request.method == "POST":
        Transaction.delete(transaction)
        if transaction_type == "Income":
            return redirect("incomes")
        elif transaction_type == "Expense":
            return redirect("bills")
        else:
            return redirect("lent")
    return render(request, "balance/deletecheck.html", {"transaction": transaction})


def details(request, id):
    transaction = get_object_or_404(Transaction, pk=id)
    items = transaction.dict().items()

    return render(
        request, "balance/details.html", {
            "transaction": transaction, "items": items}
    )


def editform(request, id):
    transaction = get_object_or_404(Transaction, pk=id)

    if request.method == "POST":
        form = TransactionForm(request.POST, instance=transaction)

        if form.is_valid():
            form.save()
            if transaction.type == "Income":
                return redirect("incomes")
            elif transaction.type == "Expense":
                return redirect("bills")
            else:
                return redirect("lent")
    else:
        form = TransactionForm(initial=transaction.__dict__)

    return render(
        request, "balance/editform.html", {
            "transaction": transaction, "form": form}
    )


def form(request):
    if request.method == "POST":
        form = TransactionForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("balance")
    else:
        form = TransactionForm()

    return render(request, "balance/form.html", {"form": form})


def incomes(request):
    return render(
        request, "balance/incomes.html", {
            "transactions": Transaction.objects.all()}
    )


def lent(request):
    return render(
        request, "balance/lent.html", {
            "transactions": Transaction.objects.all()}
    )
