from django.test import SimpleTestCase
from blog.forms import LeaveCommentForm, CityForm



class TestForm(SimpleTestCase):

	def test_leave_comment_form_isvalid(self):

		form = LeaveCommentForm(data = {
			'user': 'Admin',
			'comment_content': 'hi'
			})

		self.assertTrue(form.is_valid())

	def test_leave_comment_form_isinvalid(self):

		form = LeaveCommentForm(data = {})

		self.assertFalse(form.is_valid())
		self.assertEquals(len(form.errors), 1)

    
	def test_city_form_isvalid(self):

		form = CityForm(data = {
			'city_name': 'Minsk',
			})

		self.assertTrue(form.is_valid())

	def test_city_form_isinvalid(self):

		form = CityForm(data = {})

		self.assertFalse(form.is_valid())
		self.assertEquals(len(form.errors), 1)