from django import forms
from .models import Songs, Guitar_tabs
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from captcha.fields import CaptchaField


class FeedbackForm(forms.Form):
    name = forms.CharField(max_length=150, label='Name', widget=forms.TextInput(attrs={
        'class': "form-control",
        'type': "name",
        'id': "name",
        'placeholder': "Name"
    }))

    email = forms.CharField(max_length=150, label='Email address', widget=forms.EmailInput(attrs={
        'class': "form-control",
        'type': "email",
        'id': "email",
        # 'placeholder': "name@example.com"
        'placeholder': "Name"
    }))

    subject = forms.CharField(max_length=150, label='Subject', widget=forms.TextInput(attrs={
        'class': "form-control",
        'type': "text",
        'id': "subject",
        'placeholder': "Subject"
    }))

    message = forms.CharField(max_length=150, label='Message', widget=forms.TextInput(attrs={
        'class': "form-control",
        'type': "text",
        'id': "message",
        'placeholder': "Message",
        'cols': "30",
        'rows': "5"
    }))


# class NewUserForm(forms.Form):
#     users_email = forms.CharField(max_length=150, label='Email address', widget=forms.EmailInput(attrs={
#         'class': "form-control",
#         'type': "email",
#         'id': "floatingInput",
#         'placeholder': "name@example.com"
#     }))
#     users_password = forms.CharField(max_length=150, label='Password', widget=forms.PasswordInput(attrs={
#         'class': "form-control",
#         'type': "password",
#         'id': "floatingPassword",
#         'placeholder': "Password"
#     }))
#     remember = forms.BooleanField(label='Remember me', initial=True, widget=forms.CheckboxInput(attrs={
#         'type': "checkbox",
#         'value': "remember-me"
#     }))


class NewUserForm(UserCreationForm):
    username = forms.CharField(max_length=150, label='Username', widget=forms.TextInput(attrs={
        'class': "form-control",
        'type': "username",
        'id': "floatingInput",
        'placeholder': "example"
    }))

    email = forms.CharField(max_length=150, label='Email address', widget=forms.EmailInput(attrs={
        'class': "form-control",
        'type': "email",
        'id': "floatingInput",
        'placeholder': "name@example.com"
    }))

    password1 = forms.CharField(max_length=150, label='Password', widget=forms.PasswordInput(attrs={
        'class': "form-control",
        'type': "password",
        'id': "floatingPassword",
        'placeholder': "Password"
    }))

    # password2 = forms.CharField(max_length=150, label='Password', widget=forms.PasswordInput(attrs={
    #     'class': "form-control",
    #     'type': "password2",
    #     'id': "floatingPassword",
    #     'placeholder': "Password"
    # }))
    # remember = forms.BooleanField(label='Remember me', initial=True, widget=forms.CheckboxInput(attrs={
    #         'type': "checkbox",
    #         'value': "remember-me"
    #     }))

    class Meta:
        model = User
        fields = '__all__'


class UserForm(forms.Form):
    users_email = forms.CharField(max_length=150, label='Email address', widget=forms.EmailInput(attrs={
        'class': "form-control",
        'type': "email",
        'id': "floatingInput",
        'placeholder': "name@example.com"
    }))
    users_password = forms.CharField(max_length=150, label='Password', widget=forms.PasswordInput(attrs={
        'class': "form-control",
        'type': "password",
        'id': "floatingPassword",
        'placeholder': "Password"
    }))
