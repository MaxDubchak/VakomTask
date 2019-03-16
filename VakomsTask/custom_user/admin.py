from django.contrib import admin
from django.contrib.auth.models import Group

from custom_user.models import CustomUser


admin.site.register(CustomUser)
admin.site.unregister(Group)
