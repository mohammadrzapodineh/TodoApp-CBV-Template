from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model


User = get_user_model()
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('email', 'is_active', 'is_superuser', 'first_name', 'last_name')
    list_editable = ('is_active', 'is_superuser')
    search_fields = ('first_name', 'email', 'last_name')
    ordering = ('email',)
    fieldsets = (
        ('Auth Information', {'fields': ('email', 'password')}),
        ('User Information', {'fields': ('first_name', 'last_name')}),
        ('User Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important Dates', {'fields': ('last_login',)})
        
    )

    add_fieldsets = (
        ('Auth Information', {'fields': ('email', 'password1', 'password2')}),
        ('User Information', {'fields': ('first_name', 'last_name')}),
        ('User Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
    )