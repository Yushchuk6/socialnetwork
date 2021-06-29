from posts.serializers import PostSerializer
from rest_framework import status, viewsets, permissions
from rest_framework.decorators import action, api_view
from rest_framework.response import Response

from .models import Post
from .serializers import LikeSerializer, PostSerializer
from datetime import date
import pandas as pd


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-post_date')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    lookup_field = "title"

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @action(detail=True, methods=['put', 'delete'])
    def like(self, request, *args, **kwargs):
        snippet = self.get_object()

        good_response= {'details': 'success'}
        if request.method == "PUT":
            snippet.likes.add(self.request.user)
            return Response(good_response, status=status.HTTP_200_OK)
        elif request.method == "DELETE":
            snippet.likes.remove(self.request.user)
            return Response(good_response, status=status.HTTP_200_OK)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)

        


@api_view(['GET'])
def like_count_list(request):
    if request.method == 'GET':
        date_from = request.query_params.get('date_from')
        date_to = request.query_params.get('date_to')

        if not date_from:
            date_from = date.min
        if not date_to:
            date_to = date.max

        queryset = Post.objects.filter(post_date__range=[date_from, date_to])
        serializer = LikeSerializer(queryset, many=True)

        result = (pd.DataFrame(serializer.data)
                  .groupby(['post_date'], as_index=False)
                  .like_count.sum()
                  .to_dict('r'))

        return Response(result)
