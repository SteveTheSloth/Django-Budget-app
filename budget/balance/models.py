from django.db import models
from datetime import timedelta, date

# Create your models here.

types = (("Income", "Income"), ("Expense", "Expense"), ("Loan", "Loan"))

repeat_patterns = (
    ("one off", "one off"),
    ("monthly", "monthly"),
    ("weekly", "weekly"),
    ("every two weeks", "every two weeks"),
    ("every three weeks", "every three weeks"),
    ("every four weeks", "every four weeks"),
)


class Transaction(models.Model):
    type = models.CharField(max_length=25, choices=types, default="Expense")
    name = models.CharField(max_length=200)
    purpose = models.CharField(max_length=200)
    amount = models.FloatField(max_length=6)
    due_date = models.DateField(default=date.today())
    repeat_pattern = models.CharField(
        max_length=25, choices=repeat_patterns, default="one off"
    )
    website = models.URLField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    telephone = models.CharField(max_length=20, blank=True, null=True)
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
            "Added On": self.date_added,
        }
        return attributes

    def day_balance(self, month, year):
        if (
            self.type == "Loan"
            or self.due_date.month > month
            and self.due_date.year >= year
            or self.due_date.year > year
        ):
            return dict()
        if self.end_date != None:
            if self.end_date.month < month and self.end_date.year <= year:
                return dict()

        if self.repeat_pattern == "one off":
            return self.one_off_day()

        elif self.repeat_pattern == "monthly":
            return self.one_off_day()

        elif self.repeat_pattern == "weekly":
            return self.weekly_day(month, timedelta(weeks=1))

        elif self.repeat_pattern == "every two weeks":
            return self.weekly_day(month, timedelta(weeks=2))

        elif self.repeat_pattern == "every three weeks":
            return self.weekly_day(month, timedelta(weeks=3))

        else:
            return self.weekly_day(month, timedelta(weeks=4))

    def one_off_day(self):
        dayly_transaction_dict = dict()

        if self.type == "Expense":
            dayly_transaction_dict[self.due_date.day] = -self.amount
        else:
            dayly_transaction_dict[self.due_date.day] = self.amount

        return dayly_transaction_dict

    def weekly_day(self, month, delta):
        due_date = self.due_date
        dayly_transaction_dict = dict()

        while due_date.month != month:
            due_date += delta

        while due_date.month == month:
            if self.type == "Expense":
                dayly_transaction_dict[due_date.day] = -self.amount
            else:
                dayly_transaction_dict[due_date.day] = self.amount

            due_date += delta

        return dayly_transaction_dict

    def active_month(self, month=date.today().month, year=date.today().year):
        if (
            self.due_date.month > month
            and self.due_date.year >= year
            or self.type == "Loan"
        ):
            return 0
        elif self.end_date != None:
            if self.end_date.month < month and self.end_date.year <= year:
                return 0
            else:
                pass

        else:
            if self.repeat_pattern == "one off":
                if self.due_date.month == month:
                    if self.type == "Expense":
                        return -self.amount
                    else:
                        return self.amount
                else:
                    return 0

            elif self.repeat_pattern == "monthly":
                if self.type == "Expense":
                    return -self.amount
                else:
                    return self.amount

            elif self.repeat_pattern == "weekly":
                return self.weekly_month(month, timedelta(weeks=1))

            elif self.repeat_pattern == "every two weeks":
                return self.weekly_month(month, timedelta(weeks=2))

            elif self.repeat_pattern == "every three weeks":
                return self.weekly_month(month, timedelta(weeks=3))

            else:
                return self.weekly_month(month, timedelta(weeks=4))

    def weekly_month(self, month, delta):
        due_date = self.due_date
        amount = 0

        while due_date.month != month:
            due_date += delta

        while due_date.month == month:
            amount += self.amount
            due_date += delta

        if self.type == "Expense":
            return -amount
        else:
            return amount
