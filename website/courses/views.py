from django.shortcuts import render
from courses.models import Course

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello World!")

def get_course(request, id):
    course = Course.objects.filter(id=id)
    if(len(course) == 1):
        return HttpResponse("Course %(id)s is at row %(row)s and col %(col)s" %{'id':course[0].tag, 'row':str(course[0].row), 'col':str(course[0].col)})
    else:
        return HttpsResponse("No such Course") 
