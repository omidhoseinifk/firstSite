from django.db.models import Q
from .models import Posts
# from django.utils.translation import ugettext_lazy as _
# from django.contrib import MESSAGE
# from itertools import chain


def search(request):
    query = request.GET.get('q')
    if query:
        # tutorials = Tutorial.objects.all()
        posts = Posts.objects.all()

        # tutorials_result = tutorials.filter(
        #     Q(title__icontains=query) |
        #     Q(summary__icontains=query) |
        #     Q(description__icontains=query)
        # )
        search_result = posts.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query)
        )
        # search_result = list(chain(tutorials_result, posts_result))
        if search_result:
            return {'search_result': search_result, }
        else:
            return {'search_result': 'custom_not_found'}
    else:
        return {'search_result': None, }
