# accounts/urls.py
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # URL for user registration
    path('register/', views.register_view, name='register'),

    # URL for logging out (uses built-in LogoutView)
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # URL for password reset request page
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html'), name='password_reset'),

    # URL for password reset done (confirmation after submitting email)
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'), name='password_reset_done'),

    # URL for confirming the password reset using the token (uidb64 and token passed in URL)
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'), name='password_reset_confirm'),

    # URL for completion of password reset process
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'), name='password_reset_complete'),
]
