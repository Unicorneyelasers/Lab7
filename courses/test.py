from django.test import TestCase
from Course.models import Course

Class CourseTestCase(TestCase):
    def test_create:
        response self.client.post("/course/courses/create/", {'tag': 'F', 'row' : 3, 'col' : 4})

        c = Course.object.get(tag='F')
        self.assertEqual(c.tag, 'F')
        self.assertEqual(c.row, 3)
        self.assertEqual(c.col, 4)
    
    def duplicate_test(self):
        
        try:
            response self.client.post("/course/courses/create/", {'tag': 'F', 'row' : 3, 'col' : 4})
            if(Course.objects.get(tag='F') == 2):
                self.fail()
        except Course.DoesNotExist:
            pass

