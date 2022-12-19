from django.contrib import admin

# Register your models here.
from django.contrib import admin, messages
from django.utils.safestring import mark_safe

from tabs.models import Songs, Guitar_tabs


@admin.register(Songs)
class SongAdmin(admin.ModelAdmin):
    list_display = ['title', 'get_photo']
    readonly_fields = ('views',)

    def get_photo(self, object):
        if object.photo:
            return mark_safe(f'<img src="{object.photo.url}" width=50>')



@admin.register(Guitar_tabs)
class GuitarAdmin(admin.ModelAdmin):
        list_display = ('id', 'tab_text',)



# @admin.register.html(Piano_tabs)
# class PianoAdmin(admin.ModelAdmin):
#         list_display = ('id', 'title',)

