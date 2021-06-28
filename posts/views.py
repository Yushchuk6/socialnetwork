from posts.serializers import PostSerializer
from rest_framework import generics, mixins, viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Post
from .serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-post_date')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @action(detail=True, methods=['put', 'delete'])
    def like(self, request, *args, **kwargs):
        snippet = self.get_object()

        if request.method == "PUT":
            snippet.likes.add(self.request.user)
        elif request.method == "DELETE":
            snippet.likes.remove(self.request.user)
        
        return Response({'nice'})
    
