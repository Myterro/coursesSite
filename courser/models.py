from django.db import models
from django.utils import timezone


class Author(models.Model):
    author_name = models.CharField(max_length=40)
    author_age = models.IntegerField(default=0)
    author_photo = models.ImageField(blank=True, null=True,
                                     upload_to="authors/",
                                     default='noimg.png')

    def __str__(self):
        return self.author_name

    def author_info(self):
        return "{} is {} years old.".format(self.author_name, self.author_age)


class CourseCategory(models.Model):
    category_name = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.category_name


class Course(models.Model):
    course_name = models.CharField(max_length=80)
    pub_date = models.DateTimeField('date published', default=timezone.now())
    course_desc = models.CharField(max_length=1000)
    course_cover = models.ImageField(blank=True, null=True,
                                     upload_to="covers/%Y/%m/%D/",
                                     default='noimg.png')
    course_price = models.IntegerField(default=0)
    category = models.ForeignKey(CourseCategory, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, )

    def __str__(self):
        return self.course_name


