# accounts/forms.py
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Custom registration form for user creation
class RegisterForm(UserCreationForm):
    class Meta:
        model = User  # Use the built-in User model
        fields = ('username', 'email', 'password1', 'password2')  # Include these fields in the form

    # Customize form field attributes
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        # Add 'form-control' class to each field for consistent styling
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
