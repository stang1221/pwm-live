from django.db import models
from django.contrib.auth.models import User
from cryptography.fernet import Fernet
from django.conf import settings
from cryptography.fernet import InvalidToken

# Initialize Fernet encryption with the encryption key from settings
f = Fernet(settings.ENCRYPT_KEY)

class Password(models.Model):
    # Associate password with the user
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_passwords')
    
    # App name and username fields
    app_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, blank=True, null=True)
    
    # Store encrypted password
    password = models.CharField(max_length=255)
    
    # Timestamps for password creation and updates
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        # Encrypt the password before saving
        password_bytes = self.password.encode('utf-8')
        encrypted_password = f.encrypt(password_bytes)
        self.password = encrypted_password.decode('utf-8')
        
        super().save(*args, **kwargs)

    def get_decrypted_password(self):
        try:
            # Decrypt the password when needed
            encrypted_password = self.password.encode('utf-8')
            decrypted_password = f.decrypt(encrypted_password)
            return decrypted_password.decode('utf-8')
        except InvalidToken:
            # Return None if decryption fails
            return None

    def __str__(self):
        # String representation of the Password object
        return f"{self.app_name} - {self.user.username}"
