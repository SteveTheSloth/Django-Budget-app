from django.db import models
from django.contrib.auth.models import AbstractUser


class MyUser(AbstractUser):
    as_group = models.BooleanField(
        default=False,
    )

    group = models.CharField(max_length=50, null=True,
                             default=None, blank=True)

    def get_groups(self):
        groups = UserGroup.objects.filter(members=self.id)
        return groups

    def set_active_group(self, group):
        if group in [group.name for group in self.get_groups()]:
            self.group = group
            self.as_group = True

    def get_active_group(self):
        return UserGroup.objects.get(name=self.group)


class UserGroup(models.Model):
    name = models.CharField(max_length=50, unique=True)

    nr_of_members = models.SmallIntegerField(default=1)

    members = models.ManyToManyField(MyUser)

    password = models.CharField(max_length=35)


"""
    def get_member_ids(self):
        member_ids_int = self.members.values_list("user_id", flat=True)
        # member_ids_int = [user.id for user in self.members.all()]
        return member_ids_int

    def get_member_names(self):
        names = self.members.values_list("username", flat=True)
        # names = [user.username for user in self.members.all()]
        return names
"""
