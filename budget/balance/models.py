from django.db import models
from datetime import datetime
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

today = datetime.today()


class Item(models.Model):
    type = models.CharField(max_length=10,
                            choices=types,
                            default="Expense"
                            )

    purpose = models.CharField(max_length=200)
    amount = models.FloatField(max_length=6)
    due_date = models.DateField(null=True)
    repeat_pattern = models.CharField(max_length=30,
                                      choices=repeat_patterns,
                                      default="monthly",
                                      null=True)
    website = models.URLField(null=True)
    email = models.EmailField(null=True)
    telefone = models.PositiveBigIntegerField(null=True)
    end_date = models.DateField(null=True)
    date_added = models.DateField(default=today.strftime(
        "%d/%m/%Y"), editable=False)

    def __str__(self):
        return f"{self.type}"
