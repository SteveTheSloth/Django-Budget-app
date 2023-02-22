from django.shortcuts import render, get_object_or_404

# Create your views here.

from .models import Transaction


def balance(request):
    return render(request, "balance/balance.html")


def bills(request):
    return render(request, "balance/bills.html", {"transactions": Transaction.objects.all()})


def details(request, id):
    transaction = get_object_or_404(Transaction, pk=id)

    return render(request, "balance/details.html", {"transaction": transaction})


def incomes(request):
    return render(request, "balance/incomes.html", {"transactions": Transaction.objects.all()})


def lent(request):
    return render(request, "balance/lent.html", {"transactions": Transaction.objects.all()})
