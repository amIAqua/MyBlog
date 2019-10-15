from django.test import TestCase, Client
from django.urls import reverse, resolve
from blog.models import (Post,
                         Comment,
                         ContactAbout,
                         )




class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.MainPageView_url = reverse('blog:MainPageView')
        self.Posts24PageView_url = reverse('blog:Posts24PageView')
        self.PostPageView_url = reverse('blog:PostPageView', args = ['post1'])
        self.ContactMe_url = reverse('blog:ContactMe')
        self.post1 = Post.objects.create(
			title =  'post1',
			pub_date =  '2019-07-12 12:12',
			slug =  'post1',
			post_status =  0,
			)


    def test_main_page_view_GET(self):

        response = self.client.get(self.MainPageView_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/mainpage.html')

    def test_post_page_view_GET(self):

        response = self.client.get(self.PostPageView_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/postview.html')


    def test_post_page_view_POST_add_comment(self):

        self.comment1 = Comment.objects.create(
        	comment_body = self.post1,
			user = 'addd',
			comment_content = 'abc',
			comment_status = 1,
			)

        response = self.client.post(self.PostPageView_url, {
        	'user': 'addd',
        	'comment_content': 'abc',
        	})

        self.assertEquals(response.status_code, 302)
        self.assertEquals(self.comment1.user,  'addd')
        self.assertEquals(self.comment1.comment_content,  'abc')
        self.assertEquals(self.comment1.comment_status,  1)

    
    def test_posts24_page_view_GET(self):

        response = self.client.get(self.Posts24PageView_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/posts24.html')

    def test_contact_view_GET(self):

    	response = self.client.get(self.ContactMe_url)

    	self.assertEquals(response.status_code, 200)
    	self.assertTemplateUsed(response, 'blog/contactme.html')
