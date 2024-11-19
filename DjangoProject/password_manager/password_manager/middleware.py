import datetime
from django.conf import settings
from django.contrib.auth import logout
from django.utils.timezone import now
from datetime import timedelta
from django.contrib import messages
from django.shortcuts import redirect


class SessionTimeoutMiddleware:
    """
    Middleware to check for user inactivity and show a warning message before logging them out.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Get the last activity time from the session and parse it as a datetime object
        last_activity_str = request.session.get('last_activity', None)
        session_timeout = timedelta(minutes=30)

        if last_activity_str:
            last_activity = datetime.datetime.fromisoformat(last_activity_str)
        else:
            last_activity = None

        if last_activity and now() - last_activity > session_timeout:
            # Add message before redirecting or logging out
            messages.add_message(request, messages.WARNING, "Your session has expired due to inactivity. Please log in again.")
            return redirect('kagi:login')  # Redirect to the login page or desired page

        # Store the current time as an ISO format string in the session
        request.session['last_activity'] = now().isoformat()

        response = self.get_response(request)
        return response
