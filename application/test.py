# application/tests.py

from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post, Comment

class PostModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.post = Post.objects.create(title='Test Post', content='Content of test post', author=self.user)

    def test_post_creation(self):
        self.assertEqual(self.post.title, 'Test Post')
        self.assertEqual(self.post.content, 'Content of test post')
        self.assertEqual(str(self.post.author), 'testuser')

class CommentModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.post = Post.objects.create(title='Test Post', content='Content of test post', author=self.user)
        self.comment = Comment.objects.create(text='Test comment', author=self.user, post=self.post)

    def test_comment_creation(self):
        self.assertEqual(self.comment.text, 'Test comment')
        self.assertEqual(str(self.comment.author), 'testuser')
        self.assertEqual(str(self.comment.post), 'Test Post')
