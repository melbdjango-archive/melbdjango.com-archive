from django.db import models
from django.contrib.auth.models import User

from django_extensions.db.models import TimeStampedModel


class Event(TimeStampedModel):
    """
    An event
    """

    start_datetime = models.DateTimeField()
    finish_datetime = models.DateTimeField(null=True)

    title = models.CharField(max_length=512)
    location_name = models.CharField(max_length=512)
    author = models.ForeignKey(User)
    content = models.TextField()

    def __unicode__(self):
        return "{title} @ {location} ({author})".format(
            title=self.title,
            location=self.location_name,
            author=self.author.get_full_name() or self.author.username)
