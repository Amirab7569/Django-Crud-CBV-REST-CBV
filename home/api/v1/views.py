from django.shortcuts import get_object_or_404
# decorator that used for rest code
from rest_framework.decorators import api_view, permission_classes
# For auth in api
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework import status
from .serializers import PostSerializer
from ...models import Post
# change FBV to CBV: use API VIEW
from rest_framework.views import APIView
# Use Generic VIEW
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import mixins
# Use Viewsets
from rest_framework import viewsets
# permission
from .permissions import IsOwnerOrReadOnly
# filtering
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
# paginations
from .paginations import DefaultPagination

# Function Base View
'''
FBV post list
@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def PostList(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        # Default many = False , many for show more than one post
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
'''


"""
@api_view(['GET','PUT','DELETE'])
@permission_classes([IsAuthenticatedOrReadOnly])
def PostDetail(request, pk):
    post = Post.objects.get(pk = pk)
    if request.method == 'GET':
        serializer = PostSerializer(post)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = PostSerializer(post,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        post.delete()
        return Response({'detail':'Item remove successfully'},status=status.HTTP_204_NO_CONTENT)
"""
    
    
# CBV : API VIEW
'''
class PostList(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    # show HTML form to insert data
    serializer_class = PostSerializer

    def get(self, request):
        """
            CBV Post view 
        """
        posts = Post.objects.all()
        # Default many = False , many for show more than one post
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
        
    def post(self, request):
        """
            CBV Post Creat 
        """
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
'''
    
  
'''
class PostList(ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    # show HTML form to insert data
    serializer_class = PostSerializer
    queryset = Post.objects.all()
''' 
''' 
class PostDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    # Get post
    queryset =  Post.objects.filter(is_published=True)
'''

'''
class PostDetail(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    
    def get(self, request, pk):
        post = get_object_or_404(Post,pk = pk)
        serializer = self.serializer_class(post)
        return Response(serializer.data)
    
    def put(self, request, pk):
        post = get_object_or_404(Post,pk = pk)
        serializer = PostSerializer(post,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def delete(self, request, pk):
        post = get_object_or_404(Post,pk = pk)
        post.delete()
        return Response({'detail':'Item remove successfully'},status=status.HTTP_204_NO_CONTENT)
'''


class PostModelViewSet(viewsets.ModelViewSet):
    filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]
    permission_classes = [IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    filterset_fields = ['author','is_published']
    search_fields = ['title', 'body']
    ordering_fields = ['created']
    pagination_class = DefaultPagination