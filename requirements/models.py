from django.db import models
from login.models import UserProfile

class Comment(models.Model):
    content = models.TextField(max_length=50)

class Requirement(models.Model):
    title = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    time_posted = models.DateTimeField()
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name = "requirements")

class Queries(models.Model):
    title = models.CharField(max_length=50)
    document_id = models.CharField(max_length=50)
    status_check = models.BooleanField(default=False)
    time_posted = models.DateTimeField()
    requirement = models.ForeignKey(Requirement, on_delete=models.CASCADE)
