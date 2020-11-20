from django.shortcuts import render
from courses.models import Course, CourseEncoder
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
import json

PROGRAM_OFFSET = 3
NUMBER_OFFSET = 4

# Create your views here.
from django.http import HttpResponse

def index(request):
    course = Course.objects.all()
    return HttpResponse(json.dumps(list(course), cls=CourseEncoder))

def get_course(request, program, number):
    course = Course.objects.filter(program=program, number=number)
    if (len(course) == 1):
        return HttpResponse("%(program)s %(number)s: %(name)s" % {'program':course[0].program, 'number':str(course[0].number), 'name':course[0].name})
    else:
        return HttpResponse("No such course")

class CourseCreate(CreateView):
    model = Course
    fields = '__all__'
    success_url = reverse_lazy('index')

class CourseUpdate(UpdateView):
    model = Course
    fields = ['name']
    success_url = reverse_lazy('index')

    def get_object(self):
        requestedProgram = ''
        requestedNumber = ''
        path = self.request.path_info.split('/')
        if len(path) >= NUMBER_OFFSET:
            requestedProgram = path[PROGRAM_OFFSET]
            requestedNumber = path[NUMBER_OFFSET]
        return Course.objects.get(program=requestedProgram, number=requestedNumber)
