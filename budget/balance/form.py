from datetime import date

from django.forms import ModelForm, DateInput, TimeInput, TextInput, IntegerField, Select
from django.core.exceptions import ValidationError

from .models import Transaction


class TransactionForm(ModelForm):
    class Meta:
        model = Transaction
        fields = "__all__"
        widgets = {

        }

    def clean_date(self):
        d = self.cleaned_data.get("end_date")
        if d < date.today():
            raise ValidationError("Final Transaction can't be in the past.")
        return d
