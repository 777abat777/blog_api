from users.views import UserList
from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import PostList, CommentList

app_name = 'blog_api'


router = DefaultRouter()
router.register('posts', PostList, basename='post')
router.register('comments', CommentList, basename='comment')
router.register('users', UserList, basename='user')
urlpatterns = router.urls

# urlpatterns = [
#    path('<int:pk>/', PostDetail.as_view(), name="detailcreate"), #pk - primary key(ключевое поле)
#    path('', PostList.as_view(), name="listcreate"),
# ]
