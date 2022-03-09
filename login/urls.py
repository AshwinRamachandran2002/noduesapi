"""URLs for login."""
from django.urls import path
from login.views import LoginViewSet

urlpatterns = [
    path('login', LoginViewSet.as_view({'get': 'login'})),
    path('logout', LoginViewSet.as_view({'get': 'logout'})),
]