from django.urls import path
from django.conf.urls import url
from . import views


app_name = 'blog'

urlpatterns = [
    path('', views.MainPageView, name = 'MainPageView'),
    path('clear_list/', views.Delete_weather_list, name = 'Delete_weather_list'),
    path('posts/', views.PostsPageList.as_view(), name = 'PostsPageList'),
    path('posts/<str:slug>', views.PostPageView, name = 'PostPageView'),
    path('posts/<str:slug>/liked', views.Post_liked, name = 'Post_liked'),
    path('posts24/', views.Posts24PageView, name = 'Posts24PageView'),
    path('contact/', views.ContactMe, name = 'ContactMe'),

]