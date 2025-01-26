from django.urls import path, include
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.HomeView.as_view(),name='index'),
    path('post/<int:pk>/', views.DetailsView.as_view(),name='details'),
    path('post/create/', views.CreatePostView.as_view(),name='create'),
    path('post/update/<int:pk>/', views.UpdatePostView.as_view(),name='update'),
    path('post/delete/<int:pk>/', views.DeletePostView.as_view(),name='delete'),
    path('api/v1/', include('home.api.v1.urls'), name='api-index')
]
