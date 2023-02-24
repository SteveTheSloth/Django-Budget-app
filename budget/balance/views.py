from django.shortcuts import redirect, render, get_object_or_404

# Create your views here.

from datetime import date
from .models import Transaction
from .form import TransactionForm
from .typeselector import TypeSelector


def balance(request):
    now = date.today()
    amount = 0

    for transaction in Transaction.objects.all():
        if transaction.active_month(now.month) != None:
            if transaction.type == "Expense":
                amount -= transaction.active_month(now.month)
            elif transaction.type == "Income":
                amount += transaction.active_month(now.month)

    return render(request, "balance/balance.html", {"amount": amount})


def bills(request):
    return render(request, "balance/bills.html", {"transactions": Transaction.objects.all()})


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

    return render(request, "balance/details.html", {"transaction": transaction, "items": items})


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

    return render(request, "balance/editform.html", {"transaction": transaction, "form": form})


def form(request):
    if request.method == "POST":
        form = TransactionForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("welcome")
    else:
        form = TransactionForm()

    return render(request, "balance/form.html", {"form": form, "typeselector": TypeSelector})


def incomes(request):
    return render(request, "balance/incomes.html", {"transactions": Transaction.objects.all()})


def lent(request):
    return render(request, "balance/lent.html", {"transactions": Transaction.objects.all()})
