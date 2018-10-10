from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

app_name = 'courser'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('course/', views.CoursesListView.as_view(), name='coursesList'),
    path('course/<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('course/add/', views.AddCourseView.as_view(), name='addcourse'),
    path('author/', views.AuthorListView.as_view(), name='authorList'),
    path('author/<int:pk>/', views.AuthorView.as_view(), name='author'),
    path('author/add/', views.AddAuthorView.as_view(), name='addauthor'),
    path('api/author/', views.AuthorAPI.as_view(), name='apiauthor'),
    path('api/course/', views.CourseAPI.as_view(), name='apicourse'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.Register.as_view(), name='register'),
    path('search/', views.Search.as_view(), name='search'),
    path('categories/', views.CategoriesListView.as_view(), name='categoriesList'),
    path('categories/<int:pk>/', views.CategoriesView.as_view(), name='category'),
    path('categories/add/', views.AddCategoryView.as_view(), name='addcategory'),
    path('success/', views.success, name='success')
]