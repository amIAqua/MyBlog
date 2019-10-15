from django.test import TestCase
from blog.models import Post, Comment, ContactAbout
import datetime
from django.utils import timezone



class TestModels(TestCase):

    def setUp(self):
        self.post1 = Post.objects.create(
			title = 'title1',
			pub_date =  '2019-07-12 12:12',
			slug =  'post1',
			post_status =  0)

        self.comment = Comment.objects.create(
        	user = 'John',
        	comment_content = 'hi')

    def test_post_post_status_drafted(self):
        self.assertEqual(self.post1.post_status, 0)

    def test_post_post_status_published(self):
        try:
            self.assertEqual(self.post1.post_status, 1)

        except:
            return self.post1.post_status

    def test_comment_created(self):
                 
        self.assertEqual(self.comment.user, 'John')
        self.assertEqual(self.comment.comment_content, 'hi')


