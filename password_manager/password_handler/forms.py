from django import forms
from .models import Password

# Form to handle adding/editing passwords
class PasswordForm(forms.ModelForm):
    class Meta:
        model = Password
        fields = ['app_name', 'username', 'password']  # Fields for app name, username, and password

# Form for handling master password input (used in multi-factor authentication, for example)
class MasterPasswordForm(forms.Form):
    # Master password input field with a password widget for security
    master_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter Master Password',  # Placeholder text for the input field
    }))
