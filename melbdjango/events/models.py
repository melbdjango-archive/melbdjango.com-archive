from django.db import models
from django.contrib.auth.models import User

from django_extensions.db.models import TimeStampedModel


class Event(TimeStampedModel):
    """
    An event
    """

    start_datetime = models.DateTimeField()
    finish_datetime = models.DateTimeField(null=True)
    location_name = models.CharField(max_length=512)
    author = models.ForeignKey(User)
    content = models.TextField()
