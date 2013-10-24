import datetime

from django.db import IntegrityError
from django.test import TestCase
from django.contrib.auth.models import User

from .models import Event


class EventTests(TestCase):
    """
    Test the Event model
    """

    def setUp(self):
        self.user = User.objects.create_user(username='badger')
        self.user.save()

    def test_create_event_fails(self):
        event = Event(start_datetime=datetime.datetime(2013, 10, 24,
                                                       19, 0))

        self.assertTrue(event)

        with self.assertRaises(IntegrityError):
            event.save()

    def test_create_event(self):
        event = Event(start_datetime=datetime.datetime(2013, 10, 24,
                                                       19, 0))

        event.location_name = "Common Code"
        event.content = """This is some content"""
        event.author = self.user

        event.save()
