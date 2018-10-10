from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group


class UserCreateForm(UserCreationForm):
    username = forms.CharField(required=True, max_length=50, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    password1 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'class' : 'form-control'}))
    password2 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'class' : 'form-control'}))

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
