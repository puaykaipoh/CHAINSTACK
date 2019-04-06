from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from rest_framework.authtoken.models import Token
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
	fields = ('email', 'password', 'first_name', 'last_name', 'is_staff', 'is_active', 'is_superuser')

admin.site.register(Profile, ProfileAdmin)

admin.site.unregister(Group)
admin.site.unregister(Token)