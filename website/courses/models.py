from django.db import models
import json
from django.core.exceptions import ValidationError

# Create your models here.

def validate_case(value):
    if not value.isalpha() or not value.isupper():
        raise ValidationError('Only uppercase letters allowed', code='case_error')

class Course(models.Model):
    program = models.CharField(max_length=3, validators=[validate_case])
    number = models.IntegerField()
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.program + ' ' + str(self.number) + ': ' + self.name

    def clean(self):
        super().clean()
        course = Course.objects.filter(program=self.program, number=self.number)
        if (len(course) >= 1 and self.id == None):
            raise ValidationError('Course already exists', code='duplicate')

class CourseEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Course):
            return { 'id' : obj.id, 'program' : obj.program, 'number' : obj.number, 'name' : obj.name }
        return json.JSONEncoder.default(self, obj)

