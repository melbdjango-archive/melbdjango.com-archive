from django.test import TestCase
from django.db import IntegrityError
from django.contrib.auth.models import User

from .models import Post, POST_DRAFT, POST_PUBLISHED

# Create your tests here.
class PostsTests(TestCase):
    def setUp(self):
        self.user = User(username='test')
        self.user.save()

    def test_post_author_required(self):
        p = Post()
        p.title = 'A Common Post'
        p.content = 'This is some content'
        p.status = POST_PUBLISHED

        with self.assertRaises(IntegrityError):
            p.save()

    def test_post_title_required(self):
        p = Post()
        p.content = 'This is some content'
        p.status = POST_PUBLISHED
        p.user = self.user

        with self.assertRaises(IntegrityError):
            p.save()

    def test_post_creation(self):
        p = Post()
        p.title = 'A Common Post'
        p.content = 'This is some content'
        p.status = POST_PUBLISHED
        p.author = self.user
        p.save()

    def test_post_published_filter(self):
        posts = []
        for i in range(6):
            p = Post(
                    title='Post Title', content='Post Content',
                    author=self.user, status=POST_PUBLISHED)
            p.save()
            posts.append(p)

        self.assertEqual(Post.objects.published().count(), 6)
        
        # Now, let's set one post to draft and ensure it doesn't show up
        posts[0].status = POST_DRAFT
        posts[0].save()
        self.assertEqual(Post.objects.published().count(), 5)
        self.assertTrue(posts[0] not in Post.objects.published())
        self.assertTrue(posts[1] in Post.objects.published())
