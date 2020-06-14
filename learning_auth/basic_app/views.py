from django.shortcuts import render

# Create your views here.
from basic_app import forms
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import login, logout, authenticate

def index(request):
    return render(request,'basic_app/index.html')

def register(request):

    registered =False

    if request.method=='POST':

        user_form=forms.UserEntry(request.POST)
        user_profile_form=forms.UserProfile(request.POST)

        if user_form.is_valid() and user_profile_form.is_valid():


            user= user_form.save()
            user.set_password(user.password)
            user.save()
            profile=user_profile_form.save(commit=False)
            profile.user=user

            if 'profile_pic'in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered=True

        else:
            print('ERROR')

    else:
        user_form=forms.UserEntry()
        user_profile_form=forms.UserProfile()

    context_dict={'user_form': user_form, 'user_profile_form': user_profile_form, 'registered':  registered}
    return render(request,'basic_app/register.html', context=context_dict )

def user_login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse('Not active user')
        else:
            print('Login failed')

    return render(request, 'basic_app/login.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
