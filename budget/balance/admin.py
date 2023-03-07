from django.contrib import admin

# Register your models here.

from .models import Transaction, GroupTransaction

admin.site.register(Transaction)
admin.site.register(GroupTransaction)
