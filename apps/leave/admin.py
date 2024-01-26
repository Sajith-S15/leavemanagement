from django.contrib import admin



# Register your models here.
from .models import Leave
admin.site.register(Leave)

class UserModel(admin.ModelAdmin):
    fields = ['name', 'employee_id', 'status', 'email', 'token',
              'token_expires_at', 'role', 'password', 'team', 'batch', 'shifts']
    
    list_filter = ['name', 'email', 'role', 'team', 'batch', 'shifts', 'employee_id']
    
    list_display = fields
    search_fields = ['user_name', 'leave_type', 'duration', 'leave_status']