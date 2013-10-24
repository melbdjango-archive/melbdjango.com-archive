from django.db import models
from django.contrib.auth.models import User

POST_DRAFT = 1
POST_REVIEW = 2
POST_PUBLISHED = 3
POST_FEATURED = 4

POST_STATUS_CHOICES = (
    (POST_DRAFT, 'Draft'),
    (POST_REVIEW, 'Review'),
    (POST_PUBLISHED, 'Published'),
    (POST_FEATURED, 'Featured'),
)

class PostManager(models.Manager):
    def published(self):
        # XXX: Take in to account Post.published
        return self.all().filter(status__gte=POST_PUBLISHED)


class Post(models.Model):
    author = models.ForeignKey(User)
    title = models.CharField(max_length=200)
    slug = models.SlugField()

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    content = models.TextField()

    published = models.DateTimeField(blank=True, null=True)

    status = models.IntegerField(choices=POST_STATUS_CHOICES, default=POST_DRAFT)

    # meta_title
    # meta_description

    # tags

    objects = PostManager()

    def __unicode__(self):
        return self.title
