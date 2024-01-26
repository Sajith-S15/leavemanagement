from django.contrib import admin
from .models import User


@admin.register(User)
class UserModel(admin.ModelAdmin):
    fields = ['name', 'employee_id','status',  'email', 'token',
              'token_expires_at', 'role', 'password', 'team', 'shifts']
    list_filter = ['name','email','role', 'team', 'shifts','employee_id']
    list_display = fields
    search_fields = ['status', 'name', 'email', 'role', 'team', 'shifts', 'employee_id']
