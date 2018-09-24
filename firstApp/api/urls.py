from django.conf.urls import url
from . import views

app_name = 'api'

urlpatterns = [
    url(r'^$', views.PostListAPIView.as_view(), name='post-list'),
    url(r'^(?P<id>\d+)$',
        views.PostDetailAPIView.as_view(), name='post-detail'),
    url(r'^create/$',
        views.PostCreateAPIView.as_view(), name='post-create'),
    url(r'^(?P<id>\d+)/delete$',
        views.PostDeleteAPIView.as_view(), name='post-delete'),
    url(r'^(?P<id>\d+)/edit$',
        views.PostEditAPIView.as_view(), name='post-edit'),
    url(r'^(?P<id>\d+)/manage$',
        views.PostDeleteEditAPIView.as_view(), name='post-manage'),
]
