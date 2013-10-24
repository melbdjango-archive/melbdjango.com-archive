from django.db import models

from datetime import datetime

class Idea(models.Model):
    title = models.CharField(max_length=2048)
    description = models.TextField()

    owner = models.ForeignKey('auth.User')

    created = models.DateTimeField(default=datetime.now)

class Vote(models.Model):
    idea = models.ForeignKey('Idea')
    user = models.ForeignKey('auth.User')

    value = models.IntegerField(choices=(
        (-1, 'Down'),
        (1, 'Up'),
    ))

    class Meta:
        unique_together = (
            ('user', 'idea'),
        )

class Comment(models.Model):
    idea = models.ForeignKey('Idea')
    user = models.ForeignKey('auth.User')

    created = models.DateTimeField(default=datetime.now)

    comment = models.TextField()

    class Meta:
        ordering = ('created',)
