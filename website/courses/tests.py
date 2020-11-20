from django.test import TestCase

# Create your tests here.
from courses.models import Course

# Create your tests here.
class CourseTestCase(TestCase):
    def test_create(self):
        response = self.client.post("/courses/create/", { 'program':'ICS', 'number':113, 'name':'Operating Systems and Architecture' })
        p = Course.objects.all()
        if len(p) != 1:
            self.fail()
        else:
            self.assertEqual(p[0].program, 'ICS')
            self.assertEqual(p[0].number, 113)
            self.assertEqual(p[0].name, 'Operating Systems and Architecture')

    def test_duplicate(self):
        response = self.client.post("/courses/create/", { 'program':'ICS', 'number':113, 'name':'Operating Systems and Architecture' })
        response = self.client.post("/courses/create/", { 'program':'ICS', 'number':113, 'name':'Operating Systems and Architecture' })

        self.assertIn(b'Course already exists', response._container[0])

