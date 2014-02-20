from django.contrib import admin

from . import models

class IdeaAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'created',)

admin.site.register(models.Idea, IdeaAdmin)
admin.site.register(models.Vote)
admin.site.register(models.Comment)

