from django.forms import ModelForm
from .models import Transaction


class TypeSelector(ModelForm):
    class Meta:
        model = Transaction
        fields = ("type",)
