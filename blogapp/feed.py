from django.contrib.syndication.views import Feed

from blogapp.models import Post


class LatestEntriesFeed(Feed):
    title = "Blog title"
    link = "/feed/"
    description = "Updates on content on [blogapp title]."

    def items(self):
        return Post.objects.order_by('-published')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.teaser
