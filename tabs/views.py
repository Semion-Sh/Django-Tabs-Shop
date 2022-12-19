from aiogram.utils.mixins import DataMixin
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views.generic import CreateView
from . import models
from tabs.models import Songs, Guitar_tabs
import ssl
from .forms import NewUserForm, UserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.db import transaction


ssl._create_default_https_context = ssl._create_stdlib_context


def main(request):
    return HttpResponse(render(request, 'tabs/main.html'))


def register(request):
    return HttpResponse(render(request, 'tabs/register.html'))


def login(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            User.objects.create(**form.cleaned_data)
    else:
        form = UserForm()
    return HttpResponse(render(request, 'tabs/register.html', {'form': form}))


def sign_up(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Done!')
        else:
            messages.error(request, 'Error!')
    else:
        form = NewUserForm()
    return HttpResponse(render(request, 'tabs/signup.html', {'form': form}))


def guitar_tabs_show(request, tabs_id):
    txt = ''
    if Guitar_tabs.objects.get(id=tabs_id).tab_text != '':
        with open(Guitar_tabs.objects.get(id=tabs_id).tab_text, "r") as file:
            for i in file:
                txt += i + '|'
    tab_object = Guitar_tabs.objects.get(id=tabs_id)
    song = Songs.objects.get(guitar_tabs_id=tabs_id)
    return HttpResponse(render(request, 'tabs/guitar_tab.html', {
        'photo': song.photo,
        'title': song.title,
        'tab': txt,
    }))

    # context = {
    #     'photo': song.photo,
    #     'tittle': tab.title,
    #     'tab': tab.tab_text,
    # }
    # return render(request, 'tabs/guitar_tab.html', context=context)


def all_songs_show(request):
    context = {
        'songs': Songs.objects.all()
    }

    return render(request, 'tabs/all_songs.html', context=context)


# class RegisterUser(DataMixin, CreateView):
#     form_class = UserCreationForm
#     template_name = 'tabs/signup.html'
#     success_url = reverse_lazy('login')


def feedback(request):
    return render(request, 'tabs/feedback.html')
