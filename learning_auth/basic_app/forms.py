from django import forms
from basic_app.models import UserProfileInfo
from django.contrib.auth.models import User

class UserEntry(forms.ModelForm):
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=('username', 'email', 'password')

class UserProfile(forms.ModelForm):
    class Meta:
        model=UserProfileInfo
        fields=('profile_pic','portfolio_site')
