from django.contrib import admin
from .models import Professor, Subject, finalRatings, rating


class ProfessorAdmin(admin.ModelAdmin) :
    list_display = []
    # list_filter = ["attendanceStatus", "event"]
    for columnName in Professor._meta.fields :
        list_display.append(columnName.get_attname_column()[0])


class SubjectAdmin(admin.ModelAdmin) :
    list_display = []
    # list_filter = ["attendanceStatus", "event"]
    for columnName in Subject._meta.fields :
        list_display.append(columnName.get_attname_column()[0])

class ratingAdmin(admin.ModelAdmin) :
    list_display = []
    # list_filter = ["attendanceStatus", "event"]
    for columnName in rating._meta.fields :
        list_display.append(columnName.get_attname_column()[0])


class finalRatingsAdmin(admin.ModelAdmin) :
    list_display = []
    # list_filter = ["attendanceStatus", "event"]
    for columnName in finalRatings._meta.fields :
        list_display.append(columnName.get_attname_column()[0])

admin.site.register(finalRatings,finalRatingsAdmin)
admin.site.register(Professor,ProfessorAdmin)
admin.site.register(Subject,SubjectAdmin)
admin.site.register(rating,ratingAdmin)

# Register your models here.
