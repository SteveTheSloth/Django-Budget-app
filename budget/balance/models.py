from django.db import models
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
    type = models.TextChoices("Transaction Type", "Expense Income Loan")
    name = models.CharField(max_length=200)
    purpose = models.CharField(max_length=200)
    amount = models.FloatField(max_length=6)
    due_date = models.DateField(blank=True, null=True)
    repeat_pattern = models.TextChoices("",
                                        "once monthly weekly 2-weekly 4-weekly")
    website = models.URLField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    telephone = models.PositiveBigIntegerField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    date_added = models.DateField(auto_now_add=True, editable=False)

    def __str__(self):
        return f"{self.name}"

    def dict(self):
        attributes = {
            "Name": self.name,
            "Purpose": self.purpose,
            "Type": self.type,
            "Amount": self.amount,
            "Due On": self.due_date,
            "Repeat Pattern": self.repeat_pattern,
            "Website": self.website,
            "E-Mail": self.email,
            "Telephone Number": self.telephone,
            "End Date": self.end_date,
            "Added On": self.date_added
        }
        return attributes
