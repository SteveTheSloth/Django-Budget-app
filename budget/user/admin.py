from django.contrib import admin

# Register your models here.

from .models import UserGroup, MyUser

admin.site.register(UserGroup)
admin.site.register(MyUser)
