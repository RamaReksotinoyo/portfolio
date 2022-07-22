from django.contrib import admin
from blog.models import Post, Comment, Category

class PostAdmin(admin.ModelAdmin):
    list_display=['title', 'intro', 'date_added', 'category', 'image']
    search_fields=['title', 'intro', 'body', 'date_added', 'category', 'image']
    list_filter=('title',)
    list_per_page=4

class CommentAdmin(admin.ModelAdmin):
    list_display=['name', 'email', 'body', 'date_added']
    search_fields=['name', 'email', 'body', 'date_added']
    list_filter=('name',)
    list_per_page=4

# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Category)
