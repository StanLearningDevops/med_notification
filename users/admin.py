from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin

class CustomUserAdminConfig(UserAdmin):
    
    search_fields = ('email', 'first_name', 'last_name',)
    list_filter =('email', 'first_name', 'last_name', 'is_admin', 'is_active')
    ordering = ('-start_date',)
    list_display = ('email', 'first_name', 'last_name', 'phone_number', 'is_admin', 'is_active')
    fieldsets = (
        (None, {'fields': ('email', 'first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active','is_staff', 'is_admin')}),   
    )
    add_fieldsets=(
        (None, {
            'classes': ('wide',),
            'fields':('email', 'first_name', 'last_name', 'phone_number', 'password1', 'password2')}
        ),
    )
    
# Register your models here.
admin.site.register(CustomUser, CustomUserAdminConfig)