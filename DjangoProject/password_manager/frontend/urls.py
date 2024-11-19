# frontend/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'), # URL for the homepage view
    path('dashboard/', views.dashboard, name='dashboard'), # URL for the dashboard view (requires login)

]
