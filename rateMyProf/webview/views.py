from django.http import JsonResponse
from django.shortcuts import render


# Create your views here.
def index(request) :
    return render(request, 'webview/index.html')


def sendPassword(request) :
    print(1)
    email = request.GET.get('email', '')
    if email is not "" :

        print(email)
        return JsonResponse({"login" : "login", "avatar_url" : "url"}, status=200)
        return JsonResponse({"login": "login", "avatar_url": "url"}, status=500)
