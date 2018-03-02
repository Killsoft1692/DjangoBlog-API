from django.contrib import admin
from django.contrib.auth.models import Group
from .models import User, UserProfile

admin.site.register(User)
admin.site.register(UserProfile)
admin.site.unregister(Group)
