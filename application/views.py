# application/views.py

from rest_framework import generics, permissions
from .models import Post, Comment
from .serilizer import PostSerializer, CommentSerializer
from rest_framework.pagination import PageNumberPagination
from django.views import View


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

class IsAuthenticatedForAll(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

class PostPagination(PageNumberPagination):
    page_size = 4

class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = PostPagination
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        serializer.save(author=self.request.user)

class CommentListCreateView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        post_id = self.kwargs['post_id']
        return Comment.objects.filter(post_id=post_id)

    def perform_create(self, serializer):
        post_id = self.kwargs['post_id']
        post = Post.objects.get(id=post_id)
        serializer.save(author=self.request.user, post=post)
