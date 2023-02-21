from django.db import models
from datetime import datetime
# Create your models here.

types = (
    ("Income", "Income"),
    ("Expense", "Expense"),
    ("Loan", "Loan")
)

repeat_patterns = (
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
    due_date = models.DateField()
    repeat_pattern = models.CharField(max_length=30,
                                      choices=repeat_patterns,
                                      default="monthly")
    website = models.URLField()
    email = models.EmailField()
    telefone = models.PositiveBigIntegerField()
    end_date = models.DateField()
    date_added = models.DateField(default=today.strftime(
        "%d/%m/%Y"), editable=False, auto_created=True)

    def __str__(self):
        return f"{self.type}"
