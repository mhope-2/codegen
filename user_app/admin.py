from django.contrib import admin
from django.contrib.auth.models import User
from user_app.models import UserProfile


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email', 'first_name', 'last_name', 'is_staff']
    readonly_fields = ('id',)


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(UserProfile)