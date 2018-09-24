from firstApp.models import Posts
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import (
    SearchFilter,
    OrderingFilter,
)
from django.core.exceptions import PermissionDenied
from django.db.models import Q
from .permissions import OwnerCanManageOrReadOnly
# from .pagination import (
#     PostPageNumberPagination,
#     PostLimitOffsetPagination,
# )
from rest_framework.permissions import (
    # AllowAny,
    IsAuthenticated,
    # IsAdminUser,  # request.user.is_staff == True
    # IsAuthenticatedOrReadOnly,
)
from firstApp.api.serializers import (
    PostListSerializer,
    PostDetailSerializer,
    PostDeleteSerializer,
    PostUpdateSerializer,
    PostCreateSerializer,
    PostDeleteUpdateSerializer,
)


class PostListAPIView(generics.ListAPIView):
    # queryset = Posts.objects.all()
    serializer_class = PostListSerializer
    filter_backends = (SearchFilter, OrderingFilter, DjangoFilterBackend)
    search_fields = ('title', 'content', 'owner__username')
    ordeing_fields = ('title', 'update_date_time', 'create_date_time')
    # filter_fields = ('title', 'content', 'owner__username')

    def get_queryset(self, *args, **kwargs):
        if self.request.user.is_superuser:
            # superuser can see all posts
            queryset = Posts.objects.all()
        else:
            # otherwise every user can see his posts
            queryset = Posts.objects.filter(owner=self.request.user)

        # Custom search. It is not related to rest_framework
        query = self.request.GET.get('q')
        # q = something
        if query:
            # if user serach for something by 'q' keyword
            queryset = queryset.filter(
                Q(title__icontains=query) |
                Q(content__icontains=query) |
                Q(owner__first_name__icontains=query) |
                Q(owner__last_name__icontains=query) |
                Q(owner__username__icontains=query)
            ).distinct().order_by('-update_date_time')
        return queryset


class PostCreateAPIView(generics.CreateAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostCreateSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticated, ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        # you can send email here and etc.
        # this email sent when serializer create


class PostDetailAPIView(generics.RetrieveAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostDetailSerializer
    lookup_field = 'id'


class PostDeleteAPIView(generics.RetrieveDestroyAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostDeleteSerializer
    lookup_field = 'id'
    permission_classes = [OwnerCanManageOrReadOnly, ]

    def perform_destroy(self, serializer):
        # just owner can delete post
        if serializer.owner != self.request.user:
            raise PermissionDenied
        else:
            serializer.delete()


class PostEditAPIView(generics.RetrieveUpdateAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostUpdateSerializer
    lookup_field = 'id'
    permission_classes = [OwnerCanManageOrReadOnly, ]

    def perform_update(self, serializer):
        serializer.save(owner=self.request.user)
        # you can send email here and etc.
        # this email sent when serializer create


class PostDeleteEditAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostDeleteUpdateSerializer
    lookup_field = 'id'
    permission_classes = [OwnerCanManageOrReadOnly, ]


# with use import from the django shell
"""
from firstApp.models import Posts
from firstApp.api.serializers import PostDetailSerializer

data = {
    'title': 'this is my title',
    'content': 'this is my content',
    'owner': 1,
}
new_item = PostDetailSerializer(date=data)

if new_item.is_valid():
    new_item.save()
else:
    print(new_item.errors)
"""
