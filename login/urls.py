"""URLs for login."""
from django.urls import path
from login.views import LoginViewSet
from django.contrib import admin
from requirements.views import RequirementViewSet
urlpatterns = [
    path('login', LoginViewSet.as_view({'get': 'login'})),
    path('logout', LoginViewSet.as_view({'get': 'logout'})),
    path('admin/', admin.site.urls),
    path('get_req', RequirementViewSet.as_view({'get': 'get_requirements'}),name='template1'),
]