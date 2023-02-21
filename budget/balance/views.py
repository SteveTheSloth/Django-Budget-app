from django.shortcuts import render

# Create your views here.


def balance(request):
    return render(request, "balance/balance.html")
