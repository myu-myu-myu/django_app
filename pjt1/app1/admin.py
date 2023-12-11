from django.contrib import admin

from . import models

@admin.register(models.Music)
class PostAdmin(admin.ModelAdmin):
    list_display = ('skater', 'title', 'length', 'order', 'music')
    list_editable = ('order', )