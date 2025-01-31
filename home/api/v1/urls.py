from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

app_name = 'api-v1'

router = DefaultRouter()
router.register('post', views.PostModelViewSet, basename='post')
urlpatterns = router.urls

# urlpatterns = [
#     # path('post/', views.PostList ,name='api-post-list'),
#     # path('post/<int:pk>/', views.PostDetail ,name='api-post-detail'),
#     # path('post/', views.PostList.as_view() ,name='api-post-list'),
#     # path('post/<int:pk>/', views.PostDetail.as_view() ,name='api-post-detail'),
    # path('post/', views.PostViewSet.as_view({'get':'list','post':'create'}), name='post-list'),
    # path('post/<int:pk>/', views.PostViewSet.as_view({'get':'retrive','put':'update','patch':'partial_update','delete':'destroy'}), name='post-detail')

# ] 


