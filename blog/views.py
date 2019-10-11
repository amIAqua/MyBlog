from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.http import HttpResponseRedirect, HttpResponse
from .models import *
from .forms import LeaveCommentForm
from django.urls import reverse
from django.contrib.auth.models import User
from django.views.generic import ListView
from django.contrib import messages



def MainPageView(request):

	template_name = 'blog/mainpage.html'

	return render(request, template_name)


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
