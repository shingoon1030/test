from django.contrib import admin
from .models import User
from django.contrib.auth.models import Group

class UserAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'email',
        'time_table',
    )

admin.site.register(User)
admin.site.unregister(Group)