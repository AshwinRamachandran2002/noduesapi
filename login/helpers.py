"""Helpers for login functions."""
import requests
from django.conf import settings
from rest_framework.response import Response

def perform_login(auth_code, redir, request):
    """Perform login with code and redir."""

    post_data = 'code=' + auth_code + '&redirect_uri=' + redir + '&grant_type=authorization_code'

    # Get our access token
    response = requests.post(
        settings.SSO_TOKEN_URL,
        data=post_data,
        headers={
            "Authorization": "Basic " + settings.SSO_CLIENT_ID_SECRET_BASE64,
            "Content-Type": "application/x-www-form-urlencoded"
        }, verify=not settings.SSO_BAD_CERT)
    response_json = response.json()

    # Check that we have the access token
    if 'access_token' not in response_json:
        return Response(response_json, status=400)

    # Get the user's profile
    profile_response = requests.get(
        settings.SSO_PROFILE_URL,
        headers={
            "Authorization": "Bearer " + response_json['access_token'],
        }, verify=not settings.SSO_BAD_CERT)
    profile_json = profile_response.json()

    # Check if we got at least the user's SSO id
    if 'id' not in profile_json:
        return Response(profile_response, status=400)

    # Check that we have basic details like name and roll no.
    required_fields = ['first_name', 'roll_number', 'username']
    if not all([((field in profile_json) and profile_json[field]) for field in required_fields]):
        return Response({'message': 'All required fields not present'}, status=403)

    username = str(profile_json['id'])
    roll_no = str(profile_json['roll_number'])

    # Return the session id
    return Response({
        'sessionid': request.session.session_key,
        'username' : username,
        'roll_no' : roll_no,
    })