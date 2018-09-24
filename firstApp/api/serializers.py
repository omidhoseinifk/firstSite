from firstApp.models import Posts
from rest_framework.serializers import ModelSerializer


class PostListSerializer(ModelSerializer):
    class Meta:
        model = Posts
        fields = ('id', 'title')


class PostCreateSerializer(ModelSerializer):
    class Meta:
        model = Posts
        # fields = '__all__'
        exclude = ('owner',)


class PostDetailSerializer(ModelSerializer):
    class Meta:
        model = Posts
        fields = '__all__'


class PostDeleteSerializer(ModelSerializer):
    class Meta:
        model = Posts
        fields = '__all__'


class PostUpdateSerializer(ModelSerializer):
    class Meta:
        model = Posts
        fields = '__all__'


class PostDeleteUpdateSerializer(ModelSerializer):
    class Meta:
        model = Posts
        fields = '__all__'
