from django.contrib import admin

from .models import Event


class EventAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Event model
    """

    exclude = ('author',)

    def save_model(self, request, obj, form, change):
        """
        Save the Event model
        """

        obj.author = request.user

        super(EventAdmin, self).save_model(request, obj, form, change)

admin.site.register(Event, EventAdmin)
