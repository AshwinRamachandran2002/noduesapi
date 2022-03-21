from django.contrib import admin
from login.models import Department, UserProfile
from requirements.models import Requirement,Comment,Queries
admin.site.register(Department)
admin.site.register(UserProfile)
admin.site.register(Requirement)
admin.site.register(Comment)
# admin.site.register(Queries)
