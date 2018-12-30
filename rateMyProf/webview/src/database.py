from django.contrib.auth.models import User
from ..models import Subject,Professor, finalRatings, rating
from . import utility
import json
def addNewUser(email, password):
    try :
        u, created = User.objects.get_or_create(username=email, email=email)
        u.set_password(raw_password=password)
        u.save()
        return True
    except Exception as e :
        print(e)
        return False
    # if created:
    # # user was created
    # # set the password here
    # else:
# user was retrieved



def getSubjectList() :
    return Subject.objects.all()
    # try :
def getSubjectFromCode(code) :
    sub = Subject.objects.filter(code=code)
    if len(sub) != 1 :
        return None, False
    else :
        return sub[0], True

def getProfessor(name,depCode) :
    prof = Professor.objects.filter(name=name, departmentCode=depCode)
    print(prof)
    if len(prof) == 1 :
        return prof[0], True
    else :
        return None, False
def getProfList() :
    return  Professor.objects.all()

def getRating(subject,prof) :
    ratingObjs = finalRatings.objects.filter(subject=subject, professor=prof)
    if (len(ratingObjs) == 1) :
        return ratingObjs[0], True



def addNewrating(subject,prof,user,attendance,taMarks,grades,timing, tags) :
    try :
        print()
        rat, ratExist = rating.objects.get_or_create(subject=subject, professor=prof, user=user)
        if not ratExist :
            return "You cannot rate the same Subject and Faculty again!", False
        else :
            rat.save()
            p, created = finalRatings.objects.get_or_create(
                subject=subject,
                professor=prof,
            )
            if created :
                if attendance == 0:
                    p.numAttendance = 0
                if taMarks == 0:
                    p.numTa = 0
                if grades == 0 :
                    p.numGrade = 0
                if timing == 0 :
                    p.numTiming = 0
                p.attendance = attendance
                p.ta = taMarks
                p.grade = grades
                p.timing = timing
                p.tags = json.dumps(tags)
                p.save()
            else :
                if attendance :
                    p.attendance = utility.addValueToAverage(float(attendance), float(p.attendance), p.numAttendance)
                    p.numAttendance += 1
                if taMarks :
                    p.ta = utility.addValueToAverage(float(taMarks), float(p.ta), p.numTa)
                    p.numTa += 1
                if grades :
                    p.grade = utility.addValueToAverage(float(grades), float(p.grade), p.numGrade)
                    p.numGrade += 1
                if timing :
                    p.timing = utility.addValueToAverage(float(timing), float(p.timing), p.numTiming)
                    p.numTiming += 1

                p.tags = json.dumps(json.loads(p.tags).extend(tags))
                p.save()
            return  "Rating successfully saved", True
    except Exception as e :
        print(e)
        return str(e), False
