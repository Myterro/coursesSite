from django.views import generic
from rest_framework import generics, permissions
from .models import Course, Author, CourseCategory
from .serializers import AuthorSerializer, CourseSerializer
from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator
from django.shortcuts import render_to_response
from django.urls import reverse_lazy
from .forms import UserCreateForm


class IndexView(generic.ListView):
    template_name = 'courser/index.html'
    context_object_name = 'latest_courses'

    def get_queryset(self):
        return Course.objects.all()[:4]


class AuthorView(generic.DetailView):
    model = Author
    template_name = 'courser/author.html'


class AuthorListView(generic.ListView):
    template_name = 'courser/authorList.html'
    context_object_name = 'authors_list'
    paginate_by = 10

    def get_queryset(self):
        return Author.objects.all()


class DetailView(generic.DetailView):
    model = Course
    template_name = 'courser/detail.html'


class CoursesListView(generic.ListView):
    template_name = 'courser/coursesList.html'
    context_object_name = 'courses_list'
    paginate_by = 10

    def get_queryset(self):
        return Course.objects.all()


class CategoriesView(generic.DetailView):
    model = CourseCategory
    template_name = 'courser/category.html'
    context_object_name = 'courses_by_category'


class CategoriesListView(generic.ListView):
    template_name = 'courser/categoryList.html'
    context_object_name = 'categories_list'
    paginate_by = 10

    def get_queryset(self):
        return CourseCategory.objects.all()


@method_decorator(permission_required('addauthor.can_add', login_url='/courser/login/'), name='dispatch')
class AddAuthorView(generic.CreateView):
    model = Author
    template_name = 'courser/add.html'
    success_url = '/courser/author/'
    fields = ['author_name', 'author_age', 'author_photo']


@method_decorator(permission_required('addcourse.can_add', login_url='/courser/login/'), name='dispatch')
class AddCourseView(generic.CreateView):
    model = Course
    template_name = 'courser/add.html'
    success_url = '/courser/course'
    fields = ['course_name', 'pub_date', 'course_desc', 'course_cover', 'course_price', 'category', 'author']


@method_decorator(permission_required('addcategory.can_add', login_url='/courser/login/'), name='dispatch')
class AddCategoryView(generic.CreateView):
    model = CourseCategory
    template_name = 'courser/add.html'
    success_url = '/courser/categories'
    fields = ['category_name']


class AuthorAPI(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = (permissions.IsAuthenticated,)


class CourseAPI(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = (permissions.IsAuthenticated,)


class Search(generic.ListView):
    template_name = 'courser/coursesList.html'
    context_object_name = 'courses_list'

    def get_queryset(self):
        r = self.request.GET.get('searchInput', '')
        return Course.objects.filter(course_name__icontains=r)


class Register(generic.CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreateForm
    success_url = reverse_lazy('courser:success')

    def form_valid(self, form):
        return super().form_valid(form)


def success(request):
    return render_to_response('courser/success.html')
