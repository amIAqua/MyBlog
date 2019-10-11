from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.http import HttpResponseRedirect, HttpResponse
from .models import *
from .forms import LeaveCommentForm, CityForm
from django.urls import reverse
from django.contrib.auth.models import User
from django.views.generic import ListView
from django.contrib import messages
import requests



def MainPageView(request):

    template_name = 'blog/mainpage.html'

    app_id = '8f991c13f0503fce38aea9d673eb0f50' 
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + app_id

    if request.method == 'POST':
        form = CityForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('blog:MainPageView')) 

    form = CityForm()
   
    cities = City.objects.all()
    all_cities = []

    for city in cities:

        res = requests.get(url.format(city)).json()
    
        city_info = {

            'city': city,
            'temp': res['main']['temp'],
            'humidity': res['main']['humidity'],
            'icon': res['weather'][0]['icon']
        }

        all_cities.append(city_info)

    context = {
        'all_info': all_cities,
        'form': form,
        #'clear': d1
        }

    return render(request, template_name, context )


class PostsPageList(ListView):

    model = Post
    template_name = 'blog/posts.html'
    context_object_name = 'postslist'

    queryset = Post.objects.filter(post_status=1).order_by('-pub_date')[:10]
	#content = {'posts': posts}

	#return render(request, template_name, content)


def PostPageView(request, slug):

    template_name = 'blog/postview.html'
    post = get_object_or_404(Post, slug=slug)
    comments_list = post.comment_set.filter(comment_status=1).order_by('-pub_date')[:10]

    if request.method == 'POST':

        form = LeaveCommentForm(request.POST)

        #if user.is_authenticated():
    
        current_user = request.user.get_username()
        add_comment_content = request.POST['comment_content']                    
        post.comment_set.create(user = current_user, comment_content = add_comment_content)                
        return HttpResponseRedirect(reverse('blog:PostPageView', args = (post.slug,)))
        
        
        #messages.info(request, 'Войдите или зарегистрируйтесь, чтобы оставить комментарий')


    form = LeaveCommentForm()
                               
    content = {
	    'post': post,
	    'comments_list':comments_list,
	    'form': form	    
	    }

    return render(request, template_name, content)

"""
def Postliked(request, slug):

    template_name = 'blog/postview.html'

    post = get_object_or_404(Post, slug=slug)

    if request.method == 'POST':
        post_liked = ''
        return HttpResponseRedirect(reverse('PostPageView', args = (post.slug,)))
    
    post_liked = ''
        
        
        

   


    content = {
	    'post': post,
	    'post_liked': post_liked,
	    	    
	    }

    return render(request, template_name, content)
"""
										
def Posts24PageView(request):

	template_name = 'blog/posts24.html'

	posts = Post.objects.all().order_by('-pub_date')[:10]

	content = {
	    'posts': posts
	    } 

	return render(request, template_name, content)


def ContactMe(request):

    template_name = 'blog/contactme.html'

    personal_info = ContactAbout.objects.filter(id = 1)

    content = {
        'personal_info': personal_info
    }

    return render(request, template_name, content)
