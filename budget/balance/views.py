from django.shortcuts import redirect, render, get_object_or_404

# Create your views here.

from .models import Transaction
from .form import TransactionForm


def balance(request):
    return render(request, "balance/balance.html")


def bills(request):
    return render(request, "balance/bills.html", {"transactions": Transaction.objects.all()})


def details(request, id):
    transaction = get_object_or_404(Transaction, pk=id)
    items = transaction.dict().items()

    return render(request, "balance/details.html", {"transaction": transaction, "items": items})


def incomes(request):
    return render(request, "balance/incomes.html", {"transactions": Transaction.objects.all()})


def lent(request):
    return render(request, "balance/lent.html", {"transactions": Transaction.objects.all()})


def form(request):
    if request.method == "POST":
        form = TransactionForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("welcome")
    else:
        form = TransactionForm()

    return render(request, "balance/form.html", {"form": form})
