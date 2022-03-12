from django.db import models
from sqlalchemy import false

class Department(models.Model):
    id = models.IntegerField(max_length=50)
    name = models.CharField(max_length=100)


class User(models.Model):
    roll_no = models.IntegerField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    department = models.ForeignKey(Department)


class Admins(models.Model):
    user_id = models.IntegerField(max_length=50)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)


class Comment(models.Model):
    content = models.TextField(max_length=50)


class Requirement(models.Model):
    title = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    time_posted = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "requirements")


class Queries(models.Model):
    title = models.CharField(max_length=50)
    document_id = models.CharField(max_length=50)
    status_check = models.BooleanField(default=False)
    time_posted = models.DateTimeField()
    requirement = models.ForeignKey(Requirement, on_delete=models.CASCADE)
