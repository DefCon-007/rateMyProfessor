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
    # list_filter = ["attendanceStatus", "event"]
    # for columnName in rating._meta.fields :
    #     list_display.append(columnName.get_attname_column()[0])
    list_display = ["user", "professor", "subject"]
    # def get_name(self, obj):
    #     return obj.professor.name
    # get_name.admin_order_field  = 'prof_name'  #Allows column order sorting
    # get_name.short_description = 'Professor Name'  #Renames column head


class finalRatingsAdmin(admin.ModelAdmin) :
    list_display = []
    # list_filter = ["attendanceStatus", "event"]
    for columnName in finalRatings._meta.fields :
        list_display.append(columnName.get_attname_column()[0])
    list_display.append("get_name")
    def get_name(self, obj):
        return obj.professor.name
    get_name.admin_order_field  = 'prof_name'  #Allows column order sorting
    get_name.short_description = 'Professor Name'  #Renames column head

admin.site.register(finalRatings,finalRatingsAdmin)
admin.site.register(Professor,ProfessorAdmin)
admin.site.register(Subject,SubjectAdmin)
admin.site.register(rating,ratingAdmin)

# Register your models here.
