from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from .src import utility,database
from django.contrib.auth import authenticate, login
# Create your views here.


def index(request) :
    # if request.user.is_authenticated:

    return render(request, 'webview/index.html', {"loggedIn" : "false"})


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

def login(request) :
    username = request.POST['username'].strip()
    password = request.POST['password'].strip()

    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
    # else :
        #Invalid credentials