from django.contrib import admin

from . import models

admin.site.register(models.Idea)
admin.site.register(models.Vote)
admin.site.register(models.Comment)

