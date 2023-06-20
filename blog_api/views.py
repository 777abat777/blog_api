from django.shortcuts import render
from rest_framework import generics
from blog.models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly, SAFE_METHODS, BasePermission, DjangoModelPermissions, IsAuthenticated
from rest_framework import viewsets
from rest_framework import filters
from django.shortcuts import get_object_or_404
from rest_framework.response import Response


class PostUserWritePermission(BasePermission):
    message = 'Редактировать пост может только автор'

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user


class PostList(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer

    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get('pk')
        return get_object_or_404(Post, slug=item)
    # вернуть пост который соответствует запросу т.е. slug == запросу
    # Define Custom Queryset

    def get_queryset(self):
        return Post.objects.all()


class CommentList(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = CommentSerializer

    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get('pk')
        return get_object_or_404(Post, id=item)
    # вернуть пост который соответствует запросу т.е. slug == запросу
    # Define Custom Queryset

    def get_queryset(self):
        return Comment.objects.all()


# class PostList(viewsets.ViewSet):
#     permission_classes = [IsAuthenticated]
#     queryset = Post.postobjects.all()

#     def list(self, request):
#         serializer_class = PostSerializer(self.queryset, many=True)
#         return Response(serializer_class.data)

#     def retrieve(self, request, pk=None):
#         post = get_object_or_404(self.queryset, pk=pk)
#         serializer_class = PostSerializer(post)
#         return Response(serializer_class.data)

# def list(self, request):
#     pass

# def create(self, request):
#     pass

# def retrieve(self, request, pk=None):
#     pass

# def update(self, request, pk=None):
#     pass

# def partial_update(self, request, pk=None):
#     pass

# def destroy(self, request, pk=None):
#     pass

# class PostList(generics.ListCreateAPIView): #ListCreateAPIView используется для ендпоинтов(чтения/записи) (get/post) предоставляет коллекцию экземпляров модели
#     queryset=Post.postobjects.all() #queryset набор запросов (postobjects - кастомный выбор опубликованных постов)
#    #  permission_classes=[DjangoModelPermissionsOrAnonReadOnly] #разрешения
#    #  queryset=Post.objects.all() #objects - стандартный вывод всех постов
#     serializer_class=PostSerializer

# class PostDetail(generics.RetrieveUpdateDestroyAPIView,PostUserWritePermission): #RetrieveDestroyAPIView используется для (чтения/удаления) (get/delete)  ендпоинтов представляет один экземпляр модели.
#     queryset=Post.objects.all()
#     permission_classes=[PostUserWritePermission]
#     serializer_class=PostSerializer
