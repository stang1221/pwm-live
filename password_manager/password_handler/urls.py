from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_password, name='add_password'), # Add passwords
    path('', views.password_list, name='password_list'), # Saved passwords will be added to this list
    path('edit/<int:id>/', views.edit_password, name='edit_password'),  # Edit password
    path('delete/<int:id>/', views.delete_password, name='delete_password'),  # Delete password
    path('generate-password/', views.generate_password, name='generate_password'), # Generate complex password feature
    path('generate-password/password/', views.password, name='password'), # Generated password page
    path('decrypt/<int:id>/', views.decrypt_password, name='decrypt_password'),  # Decrypt password
]
