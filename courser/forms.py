from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from django.utils import timezone
from . import models
from .additional import generate_country_list

attrs = {'class': 'form-control',
         'onfocus': 'getCurrentId();',
         'onfocusout': 'validateForm();'}


class UserCreateForm(UserCreationForm):
    username = forms.CharField(required=True, max_length=50, widget=forms.TextInput(attrs=attrs))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs=attrs))
    password1 = forms.CharField(required=True, widget=forms.PasswordInput(attrs=attrs))
    password2 = forms.CharField(required=True, widget=forms.PasswordInput(attrs=attrs))

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
            group = Group.objects.get(name='User')
            user.groups.add(group)
        return user


class AuthorCreateForm(forms.ModelForm):
    author_name = forms.CharField(required=True, max_length=50, widget=forms.TextInput(attrs=attrs))
    author_age = forms.IntegerField(required=True, widget=forms.NumberInput(attrs=attrs))
    author_country = forms.ChoiceField(required=True, choices=[tag for tag in generate_country_list()],
                                       widget=forms.Select(attrs={'class': 'form-control'}))
    author_photo = forms.ImageField(required=True, widget=forms.FileInput(attrs=attrs))

    class Meta:
        model = models.Author
        fields = ("author_name", "author_age", "author_country", "author_photo")


class CategoryCreateForm(forms.ModelForm):
    category_name = forms.CharField(required=True, max_length=100, widget=forms.TextInput(attrs=attrs))

    class Meta:
        model = models.CourseCategory
        fields = ("category_name",)


class CourseCreateForm(forms.ModelForm):
    course_name = forms.CharField(required=True, max_length=80, widget=forms.TextInput(attrs=attrs))
    pub_date = forms.DateField(required=True, widget=forms.DateInput(attrs=attrs), initial=timezone.now().date())
    course_desc = forms.CharField(required=True, max_length=1000, widget=forms.TextInput(attrs=attrs))
    course_price = forms.IntegerField(required=True, widget=forms.NumberInput(attrs=attrs))
    category = forms.ModelChoiceField(queryset=models.CourseCategory.objects.all(), widget=forms.Select(attrs=attrs))
    author = forms.ModelChoiceField(queryset=models.Author.objects.all(), widget=forms.Select(attrs=attrs))
    course_cover = forms.ImageField(required=True, widget=forms.FileInput(attrs=attrs))

    class Meta:
        model = models.Course
        fields = ("course_name", "pub_date", "course_desc", "course_price", "category", "author", "course_cover")
