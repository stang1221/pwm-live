# password_handler/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import PasswordForm
from .models import Password
import random


@login_required
def add_password(request):
    # This view handles adding a new password for the authenticated user
    if request.method == 'POST':
        form = PasswordForm(request.POST)
        if form.is_valid():
            password_instance = form.save(commit=False)
            password_instance.user = request.user  # Associate the password with the logged-in user
            password_instance.save()
            return redirect('password_list')  # Redirect to the password list after saving
    else:
        form = PasswordForm()
    return render(request, 'password_handler/add_password.html', {'form': form})


@login_required
def password_list(request):
    # This view displays a list of passwords for the logged-in user
    passwords = Password.objects.filter(user=request.user)
    
    # Attempt to decrypt and print each password for debugging (if needed)
    for password in passwords:
        decrypted_password = password.get_decrypted_password()
        if decrypted_password:
            print(f"Decrypted password for {password.app_name}: {decrypted_password}")
        else:
            print(f"Failed to decrypt password for {password.app_name}")
    
    return render(request, 'password_handler/password_list.html', {'passwords': passwords})


@login_required
def edit_password(request, id):
    # This view handles editing an existing password
    password_instance = get_object_or_404(Password, id=id, user=request.user)

    if request.method == 'POST':
        form = PasswordForm(request.POST, instance=password_instance)
        if form.is_valid():
            form.save()
            return redirect('password_list')  # Redirect to password list after editing
    else:
        form = PasswordForm(instance=password_instance)

    return render(request, 'password_handler/edit_password.html', {'form': form})


@login_required
def delete_password(request, id):
    # This view handles deleting a password
    password_instance = get_object_or_404(Password, id=id, user=request.user)

    if request.method == 'POST':
        password_instance.delete()
        return redirect('password_list')  # Redirect to password list after deleting

    return render(request, 'password_handler/delete_password.html', {'password': password_instance})


@login_required
def generate_password(request):
    # This view simply renders the page for generating a new password
    return render(request, 'password_handler/generate_password.html')


def password(request):
    # This view generates a random password based on user-selected criteria
    length = int(request.GET.get('length'))
    uppercase = request.GET.get('uppercase')
    numbers = request.GET.get('numbers')
    symbols = request.GET.get('symbols')

    # Define the base characters for the password
    chars = list('abcdefghijklmnopqrstuvwxyz') 
    if(uppercase):
        chars.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    if(numbers):
        chars.extend('1234567890')
    if(symbols):
        chars.extend('!@#$%^&*()_+?><')
    
    # Generate the random password
    thepass = ''
    for i in range(length):
        thepass += random.choice(chars)

    return render(request, 'password_handler/password.html', {'password': thepass})


@login_required
def decrypt_password(request, id):
    # This view handles decrypting a password for the user
    password_instance = get_object_or_404(Password, id=id, user=request.user)
    decrypted_password = password_instance.get_decrypted_password()
    
    # Display the decrypted password or an error message
    if decrypted_password:
        return render(request, 'password_handler/decrypted_password.html', {
            'password_instance': password_instance, 
            'decrypted_password': decrypted_password
        })
    else:
        return render(request, 'password_handler/decrypted_password.html', {
            'password_instance': password_instance, 
            'error': 'Failed to decrypt password.'
        })
