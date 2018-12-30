from django.db import models
from django.contrib.auth.models import User
import uuid
from django.conf import settings


class Professor(models.Model) :
    name = models.CharField(max_length=75)
    departmentCode = models.CharField(max_length=10)
    website = models.URLField()
    designation = models.CharField(max_length=75)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return "{} - {}".format(self.name, settings.FACULTY_DEPARTMENT_DICT[self.departmentCode])


class Subject(models.Model) :
    code = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=150)
    credits = models.IntegerField()

    def __str__(self):
        return "{} - {}".format(self.code, self.name)


class rating(models.Model) :
    #Helps keep track of user who rated a prof and course so duplicacy is avoided
    user = models.ForeignKey(User, on_delete=models.PROTECT, default=None, related_name="user")
    professor = models.ForeignKey(Professor, on_delete=models.PROTECT, default=None, related_name="prof")
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT, default=None, related_name="subject")


class finalRatings(models.Model) :
    professor = models.ForeignKey(Professor, on_delete=models.PROTECT, default=None, related_name="finalRatingprof")
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT, default=None, related_name="finalRatingUser")
    attendance = models.DecimalField(decimal_places=2, max_digits=3, null=True)
    numAttendance = models.IntegerField(default=1, null=True)
    grade = models.DecimalField(decimal_places=2, max_digits=3, null=True)
    numGrade = models.IntegerField(default=1, null=True)
    ta = models.DecimalField(decimal_places=2, max_digits=3, null=True)
    numTa = models.IntegerField(default=1, null=True)
    timing = models.DecimalField(decimal_places=2, max_digits=3, null=True)
    numTiming = models.IntegerField(default=1, null=True)
    tags = models.TextField()