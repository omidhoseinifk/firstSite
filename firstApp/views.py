from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from firstApp.models import Posts
from django.http import Http404
from django.contrib import messages
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.utils.translation import ugettext_lazy as _
from .forms import PostForm


def list(request):
    posts = Posts.objects.all()
    paginator = Paginator(posts, 25)  # Show 25 posts per page
    page = request.GET.get('page')

    try:
        posts = paginator.get_page(page)
    except PageNotAnInteger:
        # If page not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)

    return render(request, 'list.html', {'posts': posts})


def detail(request, id=None):
    post = get_object_or_404(Posts, id=id)
    return render(request, 'detail.html', {'post': post})


def create(request):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404

    create_form = PostForm(request.POST or None, request.FILES or None,)
    if create_form.is_valid():
        create_form.save(commit=False)
        create_form.user = request.user
        post = create_form.save()
        messages.success(request, _('created successfully!!!'),
                         extra_tags='alert alert-success')
        return HttpResponseRedirect(post.get_absolute_url())
    return render(request, 'create.html', {'form': create_form})


def edit(request, id=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404

    post = get_object_or_404(Posts, id=id)
    edit_form = PostForm(request.POST or None,
                         request.FILES or None, instance=post)
    if edit_form.is_valid():
        edit_form.save()
        messages.success(request, _('updated successfully!!!'),
                         extra_tags='alert alert-success')
        return HttpResponseRedirect(post.get_absolute_url())
    return render(request, 'edit.html', {'form': edit_form})


def delete(request, id=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404

    post = get_object_or_404(Posts, id=id)
    if post.delete():
        messages.success(request, _('item deleted successfully!!!'),
                         extra_tags='alert alert-success')
        return HttpResponseRedirect('/')
    return render(request, 'detail.html', {'post': post})
