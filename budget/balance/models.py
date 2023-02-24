from django.db import models
from datetime import timedelta, date
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
    type = models.CharField(max_length=25,
                            choices=types,
                            default="Expense")
    name = models.CharField(max_length=200)
    purpose = models.CharField(max_length=200)
    amount = models.FloatField(max_length=6)
    due_date = models.DateField(default=date.today())
    repeat_pattern = models.CharField(max_length=25,
                                      choices=repeat_patterns,
                                      default="one off")
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
            "Added On": self.date_added
        }
        return attributes

    def day_balance(self, month, year):

        increase_week = timedelta(weeks=1)
        due_date = self.due_date
        dayly_transaction_dict = dict()

        if self.due_date.month > month and self.due_date.year >= year or self.type == "Loan":
            return dayly_transaction_dict
        if self.end_date != None:
            if self.end_date.month < month and self.end_date.year <= year:
                return dayly_transaction_dict

        if self.repeat_pattern == "one off":
            if self.type == "Expense":
                dayly_transaction_dict[self.due_date.day] = [-self.amount]
            else:
                dayly_transaction_dict[self.due_date.day] = [self.amount]

        if self.repeat_pattern == "monthly":
            if self.type == "Expense":
                dayly_transaction_dict[self.due_date.day] = [-self.amount]
            else:
                dayly_transaction_dict[self.due_date.day] = [self.amount]

        elif self.repeat_pattern == "weekly":
            while due_date.month != month:
                due_date += increase_week

            while due_date.month == month:

                if self.type == "Expense":
                    dayly_transaction_dict[due_date.day] = [-self.amount]
                else:
                    dayly_transaction_dict[due_date.day] = [self.amount]

                due_date += increase_week

        elif self.repeat_pattern == "every two weeks":
            increase_week = timedelta(weeks=2)

            while due_date.month != month:
                due_date += increase_week

            while due_date.month == month:

                if self.type == "Expense":
                    dayly_transaction_dict[due_date.day] = [-self.amount]
                else:
                    dayly_transaction_dict[due_date.day] = [self.amount]

                due_date += increase_week

        elif self.repeat_pattern == "every three weeks":
            increase_week = timedelta(weeks=3)

            while due_date.month != month:
                due_date += increase_week

            while due_date.month == month:

                if self.type == "Expense":
                    dayly_transaction_dict[due_date.day] = [-self.amount]
                else:
                    dayly_transaction_dict[due_date.day] = [self.amount]

                due_date += increase_week

        else:
            increase_week = timedelta(weeks=4)

            while due_date.month != month:
                due_date += increase_week

            while due_date.month == month:

                if self.type == "Expense":
                    dayly_transaction_dict[due_date.day] = [-self.amount]
                else:
                    dayly_transaction_dict[due_date.day] = [self.amount]

                due_date += increase_week

        return dayly_transaction_dict

    def active_month(self, month):
        if self.end_date != None:
            if self.end_date.month < month or self.due_date.month > month:
                return None

        if self.repeat_pattern == "one off":
            if self.due_date.month == month:
                return self.amount

        elif self.repeat_pattern == "monthly":
            return self.amount

        elif self.repeat_pattern == "weekly":

            due_in_month = self.due_date
            week = timedelta(weeks=1)
            amount = 0

            while due_in_month.month != month:
                due_in_month += week

            while due_in_month.month == month:
                amount += self.amount
                due_in_month += week

            return amount

        elif self.repeat_pattern == "every two weeks":

            due_in_month = self.due_date
            weeks = timedelta(weeks=2)
            amount = 0

            while due_in_month.month != month:
                due_in_month += weeks

            while due_in_month.month == month:
                amount += self.amount
                due_in_month += weeks

            return amount

        elif self.repeat_pattern == "every three weeks":

            due_in_month = self.due_date
            weeks = timedelta(weeks=3)
            amount = 0

            while due_in_month.month != month:
                due_in_month += weeks

            while due_in_month.month == month:
                amount += self.amount
                due_in_month += weeks

            return amount

        elif self.repeat_pattern == "every four weeks":

            due_in_month = self.due_date
            weeks = timedelta(weeks=4)
            amount = 0

            while due_in_month.month != month:
                due_in_month += weeks

            while due_in_month.month == month:
                amount += self.amount
                due_in_month += weeks

            return amount
