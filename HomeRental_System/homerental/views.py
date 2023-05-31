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

@login_required(login_url='user_login')
def update_profile(request):
    profile = request.user.profile

    if request.method == 'POST':
        profile_form = forms.UserUpdateForm(request.POST, request.FILES, instance=profile)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'profile updated successfully')
            return redirect('user_account')

    profile_form = forms.UserUpdateForm(instance=profile)
    context = {'profile_form': profile_form}
    return render(request, 'homerental/update_profile.html', context)

@login_required(login_url='user_login')
def create_homeAdd(request):
    homeadd_form = None
    if request.method == 'POST':

        homeadd_form = forms.HomeAddForm(request.POST, request.FILES)
        if homeadd_form.is_valid():
            add = homeadd_form.save(commit=False)
            add.home_owner = request.user.profile.homeowner
            homeadd_form.save()
            messages.success(request, 'Home add added successfully')
            images = request.FILES.getlist('image')
            for image in images:
                models.HomeImages.objects.create(home=add,image=image)


            return redirect('user_account')

    add_form = forms.HomeAddForm()
    images_form = forms.ImageForm()
    context = {'add_form': add_form,'images_form':images_form}
    return render(request, 'homerental/homeaddform.html', context)



@login_required(login_url='user_login')
def update_add(request, pk):
    project = models.HomeAdd.objects.get(id=pk)
    Add_form = None
    if request.method == 'POST':
        Add_form = forms.HomeAddForm(request.POST, request.FILES, instance=project)
        if Add_form.is_valid():
            Add_form.save()
            messages.success(request, 'ADD updated successfully')
            return redirect('user_account')

    Add_form = forms.HomeAddForm(instance=project)
    context = {'Add_form': Add_form}
    return render(request, 'homerental/project_form.html', context)


@login_required(login_url='user_login')
def delete_add(request, pk):
    add = models.HomeAdd.objects.get(id=pk)

    if request.method == 'POST':
        add.delete()
        messages.success(request, 'project deleted successfully')
        return redirect('user_account')

    context = {'object': add}
    return render(request, 'delete_template.html', context)


@login_required(login_url='user_login')
def createHomeAddNotification(request):
    notification_form = None
    if request.method == 'POST':
        notification_form = forms.NotificationForm(request.POST)
        if notification_form.is_valid():
            notification = notification_form.save(commit=False)
            notification.renter = request.user.profile.renter
            notification_form.save()
            messages.success(request, 'notifination added successfully')
            return redirect('user_account')

    notification_form = forms.NotificationForm()
    return render(request, 'homerental/notification_form.html', {'notification_form': notification_form})


@login_required(login_url='user_login')
def update_notification(request, pk):
    notification_form = None
    notification = models.AddNoticifation.objects.get(id=pk)
    print(notification.renter)

    if request.method == 'POST':
        notification_form = forms.NotificationForm(request.POST, instance=notification)
        if notification_form.is_valid():
            notification_form.save()
            messages.success(request, 'notification updated successfully')
            return redirect('user_account')

    notification_form = forms.NotificationForm(instance=notification)
    context = {'notification_form': notification_form}
    return render(request, 'homerental/notification_form.html', context)


@login_required(login_url='user_login')
def delete_notification(request, pk):
    notification = models.AddNoticifation.objects.get(id=pk)

    if request.method == 'POST':
        notification.delete()
        messages.success(request, 'notification  deleted successfully')
        return redirect('user_account')

    context = {'object': notification}
    return render(request, 'delete_template.html', context)


@login_required(login_url='user_login')
def delete_add(request, pk):
    add = models.HomeAdd.objects.get(id=pk)

    if request.method == 'POST':
        add.delete()
        messages.success(request, 'project deleted successfully')
        return redirect('user_account')

    context = {'object': add}
    return render(request, 'delete_template.html', context)


@login_required(login_url='user_login')
def inbox(request):
    user_messages = request.user.profile.messages.all()
    context = {'user_messages': user_messages, 'unread_massages': user_messages.filter(is_read=False).count()}
    return render(request, 'homerental/inbox.html', context)


@login_required(login_url='user_login')
def readmessage(request, pk):
    message = request.user.profile.messages.get(id=pk)
    if not message.is_read:
        message.is_read = True
        message.save()
    context = {'message': message}
    return render(request, 'homerental/message.html', context)


def sendmessage(request, pk):
    form = forms.MassegeForm()
    reciver = models.Profile.objects.get(id=pk)

    try:
        sender = request.user.profile
    except:
        sender = None
    if request.method == 'POST':
        form = forms.MassegeForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = sender
            message.reciver = reciver

            if sender:
                message.name = sender.name
                message.email = sender.email
            message.save()
            messages.success(request, 'message sent successfully!')
            if message.reciver.get_notified:
                email_body = 'To see the Message click the link below\n' + 'http://127.0.0.1:8000/user/message/' + str(
                    message.id) + '/'
                sendEmail('new message from ' + sender.name, email_body, [message.reciver.email])
                print("massege sent successfully!!")

            return redirect('user_profile', pk=reciver.id)

    context = {'form': form, 'reciver': reciver}
    return render(request, 'homerental/createmassege.html', context)


def sendEmail(subject, message, recipent):
    from_email = settings.EMAIL_HOST_USER

    send_mail(subject, message, from_email, recipent)


def notificatoinSettings(request):
    notification_form = None
    profile = request.user.profile
    if request.method == 'POST':
        notification_form = forms.Notification_settings_Form(request.POST, instance=profile)
        if notification_form.is_valid():
            form = notification_form.save()
            return redirect('inbox')

    notification_form = forms.Notification_settings_Form(instance=profile)
    return render(request, 'homerental/notification_form.html', {'notification_form': notification_form})


def complain(request, pk):
    complainForm = None
    if request.method == 'POST':
        complainForm = forms.ComplainForm(request.POST)
        complain = complainForm.save(commit=False)
        complain.complainer = request.user.profile
        complain.complainee = models.Profile.objects.get(id=pk)
        complain.save()
        print('done')
        return redirect('user_profile', pk=pk)

    complainForm = forms.ComplainForm()
    return render(request, 'homerental/complain.html', {'complainForm': complainForm})
