from django.forms import ModelForm, Form
from django.forms.widgets import ChoiceWidget
from .models import Transaction
from user.models import MyUser


class CreateTransactionForm(ModelForm):

    class Meta:
        model = Transaction
        # fields = "__all__"
        exclude = ["user", "group"]

        ''' ["name",
                  "purpose",
                  "transaction_type",
                  "amount",
                  "due_date",
                  "repeat_pattern",
                  "website",
                  "email",
                  "telephone",
                  "end_date",] '''
