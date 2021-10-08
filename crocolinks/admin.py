from crocolinks.models import CrocoLink
from django.contrib import admin
from crocolinks.models import CrocoLink


class CrocoAdmin(admin.ModelAdmin):
    list_display = ('title', 'link')

admin.site.register(CrocoLink, CrocoAdmin)