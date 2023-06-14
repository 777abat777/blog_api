from django.urls import path
from .views import PostList

app_name='blog_api'

from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('posts', PostList, basename='post')
urlpatterns = router.urls

# urlpatterns = [
#    path('<int:pk>/', PostDetail.as_view(), name="detailcreate"), #pk - primary key(ключевое поле)
#    path('', PostList.as_view(), name="listcreate"),
# ]
