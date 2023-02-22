from django.db import models
from django.utils import timezone
# Create your models here.

types = (
    ("Income", "Income"),
    ("Expense", "Expense"),
    ("Loan", "Loan")
)

repeat_patterns = (
    ("one off", "one off"),
    ("monthly", "monthly"),
    ("weekly", "weekly"),
    ("every two weeks", "every two weeks"),
    ("every three weeks", "every three weeks"),
    ("every four weeks", "every four weeks"),
)


class Transaction(models.Model):
    type = models.CharField(max_length=10,
                            choices=types,
                            default="Expense"
                            )
    name = models.CharField(max_length=200)
    purpose = models.CharField(max_length=200)
    amount = models.FloatField(max_length=6)
    due_date = models.DateField(blank=True, null=True)
    repeat_pattern = models.CharField(max_length=30,
                                      choices=repeat_patterns,
                                      default="monthly")
    website = models.URLField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    telefone = models.PositiveBigIntegerField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    date_added = models.DateField(default=timezone.now(), editable=False)

    def __str__(self):
        return f"{self.type}"
