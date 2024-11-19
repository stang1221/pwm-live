from django.contrib import admin
from .models import Password

# Register the Password model to the Django admin interface
@admin.register(Password)
class PasswordAdmin(admin.ModelAdmin):
    # Define which fields to display in the list view
    list_display = ('app_name', 'username', 'password', 'user', 'created_at', 'updated_at')
    # You can also add more customization options if necessary, like filters or search fields
