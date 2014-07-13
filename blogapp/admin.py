from django.contrib import admin

from blogapp.models import Post
from blogapp.models import Image


class PostAdmin(admin.ModelAdmin):
    # fields display on change list
    list_display = ['title']
    # fields to filter the change list with
    list_filter = ['published', 'created']
    # fields to search in change list
    search_fields = ['title', 'content']
    # enable the date drill down on change list
    # date_hierarchy = 'created'
    # enable the save buttons on top on change form
    save_on_top = True
    # prepopulate the slug from the title - big timesaver!
    prepopulated_fields = {"slug": ("title",)}


class ImageAdmin(admin.ModelAdmin):
    list_display = ['title']
    save_on_top = True


admin.site.register(Post, PostAdmin)
admin.site.register(Image, ImageAdmin)