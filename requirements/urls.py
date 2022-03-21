"""URLs for login."""
from django.urls import path
from requirements.views import RequirementViewSet

urlpatterns = [
    path('get_req', RequirementViewSet.as_view({'get': 'get_requirements'})),
    # path('logout', RequirementViewSet.as_view({'get': 'logout'})),
]