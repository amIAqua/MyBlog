from django.test import SimpleTestCase
from django.urls import reverse, resolve
from blog.views import ( MainPageView,
                         PostsPageList,
                         Posts24PageView,
                         PostPageView,
                         ContactMe,
                         Delete_weather_list,
                         Post_liked,
                       )


class TestUrls(SimpleTestCase):

	def test_main_page_url_resolves(self):
		url = reverse('blog:MainPageView')
		self.assertEquals(resolve(url).func, MainPageView)

	def test_posts_page_resolves(self):
		url = reverse('blog:PostsPageList')
		self.assertEquals(resolve(url).func.view_class, PostsPageList)

	def test_posts24_page_url_resolves(self):
		url = reverse('blog:Posts24PageView')
		self.assertEquals(resolve(url).func, Posts24PageView)

	def test_current_post_page_url_resolves(self):
		url = reverse('blog:PostPageView', args = ['any-slug'])
		self.assertEquals(resolve(url).func, PostPageView)

	def test_contact_page_url_resolves(self):
		url = reverse('blog:ContactMe')
		self.assertEquals(resolve(url).func, ContactMe)

	def test_delete_weather_list_url_resolves(self):
		url = reverse('blog:Delete_weather_list')
		self.assertEquals(resolve(url).func, Delete_weather_list)

	def test_post_liked_url_resolves(self):
		url = reverse('blog:Post_liked', args = ['any-slug'])
		self.assertEquals(resolve(url).func, Post_liked)

