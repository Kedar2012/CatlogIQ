from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User,UserProfile

@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ('User_Name', 'Email', 'First_Name', 'Last_Name', 'Role', 'is_admin', 'is_staff', 'is_active')
    search_fields = ('User_Name', 'Email', 'First_Name', 'Last_Name', 'Role')
    readonly_fields = ('date_joined', 'last_login', 'modified_date')
    ordering = ('date_joined',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at')