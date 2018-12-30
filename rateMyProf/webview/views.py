from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from .src import utility,database
from django.contrib.auth import authenticate, login
import json
from django.conf import settings
# Create your views here.


def index(request, newContext={}) :
    context = {}
    context.update(newContext)
    context["subjects"] = []
    context["prof"] = []
    for sub in database.getSubjectList() :
        context["subjects"].append(str(sub))

    for prof in database.getProfList() :
        context["prof"].append(str(prof))

    if request.user.is_authenticated:
        context["loggedIn"] = "true"
    else :
        context["loggedIn"] = "false"

    return render(request, 'webview/index.html', context)


def sendPassword(request) :
    email = request.GET.get('email', '')
    errorMsg = "Some error occurred. Please try again later"

    if email is not "" :
        if "@iitkgp.ac.in" in email :
            password = utility.getPassword()
            status = database.addNewUser(email,password)
            if status:
                mailStatus = utility.sendMail(email,password)
                if mailStatus :
                    return HttpResponse("success", status=200)

    return HttpResponse(errorMsg, status=500)

def Userlogin(request) :
    username = request.POST['email'].strip()
    password = request.POST['password'].strip()

    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return index(request, {"isLoginSuccess" : True})

    # else :
        #Invalid credentials

def addRating(request) :
    data = json.loads(request.body)
    print(data)
    errorMsg = "Some internal error occurred, Please try again"
    subDataList  = data["subject"].split("-")
    subject, Sstatus = database.getSubjectFromCode(subDataList[0].strip())
    profDataList = data["prof"].split("-")
    prof, Pstatus = database.getProfessor(profDataList[0].strip(), settings.FACULTY_DEPARTMENT_DICT_REVERSE[profDataList[1].strip()])
    tagsList = []
    if data["tags"] is not "" :
        for tag in json.loads(data["tags"]) :
            tagsList.append(tag["value"])
    if Sstatus and Pstatus :
        try :
            print("Getting rating")
            attendance = int(data.get("attendance", 0))
            taMarks = int(data.get("taMarks", 0))
            grades = int(data.get("grades", 0))
            timing = int(data.get("timing", 0))
            msg, status = database.addNewrating(subject,prof,request.user,attendance, taMarks, grades, timing, tagsList)
            if status :
                return JsonResponse({"swalStatus" : "success", "msg" : "Rating successfully submitted"}, status=200)
            else :
                errorMsg = msg
        except Exception as e :
            errorMsg = "Some unknown error occurred. Please try again later"
            print(e)
    else :
        errorMsg = "Invalid subject or professor, Please try again"
    #
    # if Sstatus and Pstatus:
    #     try :
    #
    #         attendance = data["subject"]
    #         # if request.user.is_authenticated :
    #         #     for key,value in data.items() :
    #         #         if key == "subject" or prof :
    #
    #
    #         else :
    #             errorMsg = "Unauthenticated user. Please log in again!"
    #     except Exception as e :
    #         print(e)
    return  JsonResponse({"msg" : errorMsg, "swalStatus" : "error"}, status=400)
    # subList = database.getSubjectList()