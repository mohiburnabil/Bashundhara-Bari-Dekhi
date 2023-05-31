"""
URL configuration for HomeRentalSystem project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('user/account/', views.user_account, name='user_account'),
    path('user/login/', views.user_login, name='user_login'),
    path('user/register/', views.register, name='register'),
    path('Adds/<str:pk>/', views.Add, name='add'),
    path('user/logout/', views.user_logout, name='user_logout'),
    path('user/account/update-profile/', views.update_account, name='update_profile'),
    path('create-homeAdd/', views.create_homeAdd, name='create_homeAdd'),
    path('update-homeAdd/<str:pk>/', views.update_add, name='update-add'),
    path('delete-homeAdd/<str:pk>/', views.delete_add, name='delete-add'),
    path('user/<str:pk>/', views.user_profile, name='user_profile'),
    path('inbox/', views.inbox, name='inbox'),
    path('inbox/settings/', views.notificatoinSettings, name='notificationSettings'),
    path('user/notification', views.createHomeAddNotification, name='addNotification'),
    path('user/notification_update/<str:pk>/', views.update_notification, name='updateNotification'),
    path('user/delete-notification/<str:pk>/', views.delete_notification, name='delete_notification'),
    path('user/message/<str:pk>/', views.readmessage, name='readmessage'),
    path('user/sendmessage/<str:pk>/', views.sendmessage, name='sendmessage'),
    path('user/complain/<str:pk>/', views.complain, name='complain')
]
