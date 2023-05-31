from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from. import models
from django import forms


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'email', 'username', 'password1', 'password2']
        labels ={
           'first_name':'name'
        }
    Sign_UP_as_a_home_owner = forms.BooleanField()


    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})
 class UserUpdateForm(ModelForm):
    class Meta:
        model = models.Profile
        fields = ['name', 'profile_image', 'email', 'phone', 'show_phone_number', 'location', 'social_facebook']

    def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})

class DateInput(forms.DateInput):
    input_type = 'date'
class HomeAddForm(ModelForm):
    class Meta:
        model = models.HomeAdd
        fields = ['block_name', 'road_num', 'house_num', 'house_details','available_from', 'thumbnil', 'rent_ammount', 'house_type']
        widgets = {'available_from':DateInput()}
    def __init__(self, *args, **kwargs):
        super(HomeAddForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})



class ImageForm(ModelForm):
    class Meta:
        model = models.HomeImages
        fields = ['image']

    def __init__(self, *args, **kwargs):
        super(ImageForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})


class NotificationForm(ModelForm):
    class Meta:
        model = models.AddNoticifation
        fields = ['block_name', 'road_number', 'maximum_rent_ammount']

    def __init__(self, *args, **kwargs):
        super(NotificationForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})


class MassegeForm(ModelForm):
    class Meta:
        model = models.Message
        fields = ['body']

    def __init__(self, *args, **kwargs):
        super(MassegeForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})


class Notification_settings_Form(ModelForm):
    class Meta:
        model = models.Profile
        fields = ['get_notified']

    def __init__(self, *args, **kwargs):
        super(Notification_settings_Form, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})


class ComplainForm(ModelForm):
    class Meta:
        model = models.Complain
        fields = ['complain']

    def __init__(self, *args, **kwargs):
        super(ComplainForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})
