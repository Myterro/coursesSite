from django.test import TestCase
from .models import Author, Course


class AuthorModelTest(TestCase):
    def test_string_repr(self):
        author = Author(author_name="Tomasz")
        self.assertEqual(str(author), author.author_name)

class CourseModelTest(TestCase):
    def test_string_repr(self):
        course = Course(course_name="Python")
        self.assertEqual(str(course), course.course_name)