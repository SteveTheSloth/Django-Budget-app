from django.forms import ModelForm
from .models import Transaction


class CreateTransactionForm(ModelForm):

    class Meta:
        model = Transaction
        # fields = "__all__"
        exclude = ["user"]

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
