from django.contrib import admin
from .models import Professor, Subject


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


admin.site.register(Professor,ProfessorAdmin)
admin.site.register(Subject,SubjectAdmin)

# Register your models here.
