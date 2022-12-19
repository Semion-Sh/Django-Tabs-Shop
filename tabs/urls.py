from django.contrib import admin
from django.urls import path
from .views import all_songs_show, guitar_tabs_show, register, sign_up, main, feedback
from django.contrib import admin
from django.views.decorators.cache import cache_page


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main),
    path('all-songs', cache_page(60 * 59)(all_songs_show)),
    path('tab/<int:tabs_id>/', cache_page(60)(guitar_tabs_show), name='tab'),
    path('login', cache_page(60 * 59)(register)),
    path('sign-up', cache_page(60 * 59)(sign_up)),
    path('feedback', feedback),
]
