from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from rest_framework.authtoken.models import Token
from .models import Profile

admin.site.register(Profile)

admin.site.unregister(Group)
admin.site.unregister(Token)