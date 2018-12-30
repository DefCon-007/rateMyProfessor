import string
import random
import sendgrid
from django.conf import settings
from sendgrid.helpers.mail import *
from sentry_sdk import capture_message
from django.shortcuts import redirect

def redirect_with_context(request, to, context):
    request.session['redirect_context'] = context
    return redirect(to)

def getPassword(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def addValueToAverage(val,avg, num) :
    newAvg = avg + ((val -avg)/(num+1))
    return  newAvg

def sendMail(email, password) :
    sg = sendgrid.SendGridAPIClient(apikey=settings.SENDGRID_API_KEY)
    from_email = Email("support@ratemyprof.defcon007.com")
    to_email = Email(email)
    subject = "RateMyProf password"
    content = Content("text/plain", "Your password is {}. Please login using your email address and given password to rate.".format(password))
    mail = Mail(from_email, subject, to_email, content)
    mail.reply_to = Email("ayushgoyal.iitkgp@gmail.com")
    response = sg.client.mail.send.post(request_body=mail.get())
    if 200 <= response.status_code < 300:
        return True
    else:
        capture_message(f"Unable to send password to {email}\nStatus : {response.status_code}\nResponse : {response.body}")
        return False
    # print(response.status_code)
    # print(response.body)
    # print(response.headers)


