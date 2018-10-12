from django.views import generic
from rest_framework import generics, permissions
from .models import Course, Author, CourseCategory
from .serializers import AuthorSerializer, CourseSerializer
from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator
from django.shortcuts import render_to_response
from django.urls import reverse_lazy
from . import forms


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
    template_name = 'courser/addAuthor.html'
    form_class = forms.AuthorCreateForm
    success_url = '/courser/author/'

    def form_valid(self, form):
        return super().form_valid(form)


@method_decorator(permission_required('addcourse.can_add', login_url='/courser/login/'), name='dispatch')
class AddCourseView(generic.CreateView):
    template_name = 'courser/addCourse.html'
    form_class = forms.CourseCreateForm
    success_url = '/courser/course/'

    def form_valid(self, form):
        return super().form_valid(form)


@method_decorator(permission_required('addcategory.can_add', login_url='/courser/login/'), name='dispatch')
class AddCategoryView(generic.CreateView):
    template_name = 'courser/addCategory.html'
    form_class = forms.CategoryCreateForm
    success_url = '/courser/category/'

    def form_valid(self, form):
        return super().form_valid(form)


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
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('courser:success')

    def form_valid(self, form):
        return super().form_valid(form)


def success(request):
    return render_to_response('courser/success.html')
