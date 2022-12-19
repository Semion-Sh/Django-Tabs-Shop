from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('tabs.urls')),
    path('captcha/', include('captcha.urls')),
]
