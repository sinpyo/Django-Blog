from django.contrib import admin
from blog.models import Category, Board, Post, Comment

# Register your models here.
admin.site.register(Comment)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'cat_name']
    list_display_links = ['cat_name']
    list_per_page = 10
    search_fields = ['cat_name']


@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    list_display = ['id', 'cat_id', 'bd_name', 'bd_right']
    list_display_links = ['bd_name']
    list_per_page = 10
    search_fields = ['bd_name']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'cat_id', 'board_id', 'post_name', 'content', 'post_modifydate']
    list_display_links = ['post_name']
    list_per_page = 10
    #    list_filter = ['']
    search_fields = ['post_name']

    def content(self, post):
        return post.post_content[:10]
