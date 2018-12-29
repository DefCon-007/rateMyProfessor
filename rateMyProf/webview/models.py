from django.db import models
import uuid


class Professor(models.Model) :
    name = models.CharField(max_length=50)
    departmentCode = models.CharField(max_length=5)
    website = models.URLField()
    designation = models.CharField(max_length=50)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)


class Subject(models.Model) :
    code = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=50)
    credits = models.IntegerField()