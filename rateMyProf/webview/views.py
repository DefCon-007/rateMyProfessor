from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from .src import utility,database
# Create your views here.
def index(request) :
    return render(request, 'webview/index.html')


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

