from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from myuser.models import MyUser
# Register your models here.


class MyUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('display_name', 'age', 'homepage', )}),
    )


admin.site.register(MyUser, MyUserAdmin)
