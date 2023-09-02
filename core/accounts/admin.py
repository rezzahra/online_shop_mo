from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User, OtpCode


class CustomUserAdmin(UserAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm

    list_display = ('email', 'phone_number', 'is_admin')
    list_filter = ('is_admin',)

    fieldsets = (
        (None, {'fields': ('email', 'phone_number', 'full_name', 'password')}),
        ("Permission", {"fields": ("is_active", "is_admin", "last_login")}),
    )

    add_fieldsets = (
        (None, {'fields': ('phone_number', 'email', 'full_name', 'password1', 'password2')}),
    )

    search_fields = ('email', 'full_name')
    ordering = ('full_name',)
    filter_horizontal = ()


class OtpCodeAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'code', 'created_date')


admin.site.unregister(Group)
admin.site.register(User, CustomUserAdmin)
admin.site.register(OtpCode, OtpCodeAdmin)
