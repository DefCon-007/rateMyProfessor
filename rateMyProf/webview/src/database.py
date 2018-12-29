from django.contrib.auth.models import User


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