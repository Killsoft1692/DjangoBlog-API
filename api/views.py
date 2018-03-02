from blog.models import Post
from api.serializers import PostSerializer
from rest_framework.generics import ListAPIView


class PostListView(ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        queryset = Post.objects.all()

        return queryset


