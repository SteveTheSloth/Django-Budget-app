from django.shortcuts import render

# Create your views here.


def balance(request):
    return render(request, "balance/balance.html")


def bills(request):
    return render(request, "balance/bills.html")


def details(request):
    return render(request, "balance/details.html")


def incomes(request):
    return render(request, "balance/incomes.html")


def lent(request):
    return render(request, "balance/lent.html")
