from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from login.serializer import UserProfileFullSerializer
from django.utils import timezone
from login.models import UserProfile
from login.settings import *

class RequirementViewSet(viewsets.ViewSet):
    
    
    def get_requirements(request):
        """Get requirements."""

        # Check if the user is authenticated
        if not request.user.is_authenticated:
            return Response({"message": "not logged in"}, status=401)

        # Check if the user has a profile
        try:
            queryset = UserProfileFullSerializer.setup_eager_loading(UserProfile.objects)
            user_profile = queryset.get(user=request.user)
        except UserProfile.DoesNotExist:
            return Response({'message': "UserProfile doesn't exist"}, status=500)

        roll_no = user_profile.roll_no
        if roll_no not in ADMIN_URLS:
            return Response({'message': "Does not have permissions"})

        # Count this as a ping
        user_profile.last_ping = timezone.now()
        user_profile.save(update_fields=['last_ping'])

        users_from_department = user_profile.department.get_students()
        user_requirement_data = users_from_department.get_requirements()
        print(user_requirement_data)
        # Return the details and nested profile
        # return Response({
        #     'sessionid': request.session.session_key,
        #     'requirements' : user_requirement_data.json(),
        # })
