# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm

# View for handling user registration
def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)  # Initialize form with POST data
        if form.is_valid():
            form.save()  # Save the new user
            messages.success(request, 'Account created successfully! You can now log in.')
            return redirect('kagi:login')  # Redirect to login page
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = RegisterForm()  # Initialize an empty form for GET request

    return render(request, 'accounts/register.html', {'form': form})  # Render the form
