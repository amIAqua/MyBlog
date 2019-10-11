from django.urls import path
from django.conf.urls import url
from . import views


app_name = 'blog'

urlpatterns = [
    path('', views.MainPageView, name = 'MainPageView'),
    path('posts/', views.PostsPageList.as_view(), name = 'PostsPageList'),
    path('posts/<str:slug>', views.PostPageView, name = 'PostPageView'),
    #path('posts/<str:slug>/liked', views.Postliked, name = 'Postliked'),
    path('posts24/', views.Posts24PageView, name = 'Posts24PageView'),
    path('contact/', views.ContactMe, name = 'ContactMe'),

]