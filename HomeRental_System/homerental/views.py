from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from . import models
from . import forms

# Create your views here.


def home(request):
    return  render(request,'homerental/adds.html')


# Create your views here.

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = models.User.objects.get(username=username)

        except:
            messages.error(request, 'user not found')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'user successfully logged in')
            return redirect(request.GET['next'] if 'next' in request.GET
                            else 'user_account')
        else:
            messages.error(request, 'username or password incorrect')

    return render(request, 'homerental/login_register.html')


def register(request):
    form = forms.UserRegisterForm()
    if request.method == 'POST':
        print(request.POST['Sign_UP_as_a_home_owner'])

        try:
            models.Profile.objects.get(email=request.POST['email'])
            messages.error(request, 'Email already exist')

        except:
            form = forms.UserRegisterForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                user.username = user.username.lower()
                user.save()
                print("cheking checking")
                homeowner=False
                if request.POST['Sign_UP_as_a_home_owner']:
                    print("true")
                    homeowner =True
                else:
                    print("false")
                    homeowner=False

                new_profile = models.Profile.objects.create(
                    user=user,
                    email=user.email,
                    name=user.username,
                    is_homeowner=homeowner
                )

                if(homeowner):
                    models.HomeOwner.objects.create(user_profile=new_profile)
                else:
                    models.Renter.objects.create(user_profile=new_profile)


                login(request, user)
                messages.success(request, 'user account was created')
                return redirect('user_account')

            else:
                messages.error(request, 'error occurred')

    page = 'register'
    context = {'page': page, 'form': form}
    return render(request, 'homerental/login_register.html', context)


@login_required(login_url='user_login')
def user_logout(request):
    logout(request)
    messages.info(request, 'user succesfully logged out')

@login_required(login_url='user_login')
def user_account(request):
    user = request.user
    context = {'user': user}
    return render(request, 'homerental/account.html', context)
