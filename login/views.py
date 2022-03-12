"""Login Viewset."""
from django.conf import settings
from django.contrib.auth import logout
from rest_framework import viewsets
from rest_framework.response import Response
from login.helpers import perform_login

class LoginViewSet(viewsets.ViewSet):
    """Login"""

    @staticmethod
    def login(request):
        """Log in.
        Uses the `code` and `redir` query parameters."""

        # Check if we have the auth code
        auth_code = request.GET.get('code')
        if auth_code is None:
            return Response({"message": "{?code} is required"}, status=400)

        # Check we have redir param
        redir = request.GET.get('redir')
        if redir is None:
            return Response({"message": "{?redir} is required"}, status=400)

        return perform_login(auth_code, redir, request)

    @staticmethod
    def logout(request):
        """Log out."""

        logout(request)
        return Response({'message': 'logged out'})