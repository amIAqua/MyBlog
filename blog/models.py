from django.db import models
from django.utils import timezone
import datetime
from django.contrib.auth.models import User
#from . import settings

POST_STATUS = (
    (0,"Drafted"),
    (1,"Published")
	)

class Post(models.Model):
    
    title = models.CharField(max_length = 100)
    pub_date = models.DateTimeField()
    slug = models.SlugField(default = '')
    post_content = models.TextField(blank = True)
    post_status = models.IntegerField(choices=POST_STATUS, default=0)
    

    def __str__(self):
        return self.title #+ ', ' + str(self.pub_date.strftime("%m/%d/%Y, %H:%M"))

    def was_published_recently(self):
        return self.pub_date >= (timezone.now() - datetime.timedelta(hours = 4))

    def was_published_before24(self):
        return self.pub_date >= (timezone.now() - datetime.timedelta(hours = 24))

COMMENT_STATUS = (
    (0,"Drafted"),
    (1,"Published")
	)  

class Comment(models.Model):

    comment_body = models.ForeignKey(Post, on_delete = models.CASCADE, null=True)

    #user = models.ForeignKey(User, on_delete= models.CASCADE, related_name = 'commenter')
    user = models.CharField(max_length = 100)
    pub_date = models.DateTimeField(auto_now_add = True)
    comment_content = models.TextField(default= '')
    comment_status = models.IntegerField(choices=COMMENT_STATUS, default=1)

    def __str__(self):
        return str(self.user)


class ContactAbout(models.Model):

	name = models.CharField(max_length = 40)
	surname = models.CharField(max_length = 50)
	city_of_living = models.CharField(max_length = 30)
	country_of_living = models.CharField(max_length = 30)
	age = models.CharField(max_length = 100)

	def __str__(self):
		return self.name + ' ' + self.surname

    #class Meta():

        #verbose_name = 'AboutMe'



        




    
	




