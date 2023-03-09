from django.db import models
from django.db.models import ForeignKey, ManyToManyField
from django.db.models.fields import CharField, SmallIntegerField, IntegerField
from django.forms import ModelForm
from django.forms.widgets import ChoiceWidget
from django.contrib.auth.models import AbstractUser


# Create your models here.


class MyUser(AbstractUser):
    as_group = models.CharField(
        max_length=10, null=True, default=False, choices=[(True, "True"), (False, "False")])

    group = models.CharField(max_length=50, null=True,
                             default=None, blank=True)

    def get_groups(self):
        groups = UserGroup.objects.filter(members=self.id)
        return groups

    def set_active_group(self, group):
        if group in [x.name for x in self.get_groups()]:
            self.group = group
            self.as_group = True

    def get_active_group(self):
        return UserGroup.objects.get(name=self.group)


class UserGroup(models.Model):
    name = CharField(max_length=50, unique=True)

    nr_of_members = SmallIntegerField(default=1)

    members = ManyToManyField(MyUser)

    password = CharField(max_length=35)

    def get_member_ids(self):
        member_ids_int = [x.id for x in self.members.all()]
        return member_ids_int

    def get_member_names(self):
        names = [x.username for x in self.members.all()]
        return names
