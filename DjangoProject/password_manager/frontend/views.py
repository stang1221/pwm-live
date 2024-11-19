# frontend/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# View for rendering the homepage
def homepage(request):
    return render(request, 'frontend/homepage.html')

# View for rendering the dashboard (only accessible to logged-in users)
@login_required
def dashboard(request):
    return render(request, 'frontend/dashboard.html')  # Render the dashboard.html template
