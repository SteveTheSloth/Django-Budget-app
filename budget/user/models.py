from django.db import models
from django.db.models import ForeignKey, ManyToManyField
from django.db.models.fields import CharField, SmallIntegerField
from django.contrib.auth.models import User, Group

# Create your models here.


class UserGroup(models.Model):
    name = CharField(max_length=50, unique=True)

    nr_of_members = SmallIntegerField(default=1)

    members = ManyToManyField(User)

    password = CharField(max_length=35)

    def get_member_ids(self):
        member_ids_int = [x.id for x in self.members.all()]
        return member_ids_int

    def get_member_names(self):
        names = [x.username for x in self.members.all()]
        return names
