from django.contrib import admin
from .models import Post, Comment, ContactAbout, City


class PostAdmin(admin.ModelAdmin):

    list_display = ('title', 'slug', 'post_status', 'pub_date')
    list_filter = ("post_status",)
    search_fields = ['title']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post, PostAdmin)


class CommentAdmin(admin.ModelAdmin):

    list_display = ('comment_body', 'user', 'comment_status', 'pub_date')
    list_filter = ("comment_status",)
    search_fields = ['user']
    #prepopulated_fields = {'slug': ('title',)}

admin.site.register(Comment, CommentAdmin)


class ContactsAdmin(admin.ModelAdmin):

    list_display = ('name', 'surname', 'age', 'city_of_living', 'country_of_living')
    search_fields = ['name']
    
admin.site.register(ContactAbout, ContactsAdmin)

admin.site.register(City)
